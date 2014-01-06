import exifread
from PIL import Image
from sqlalchemy import Column, ForeignKey, types, orm
from pyramid_frontend.images.utils import is_white_background

from .base import Base


class Photo(Base):
    __tablename__ = 'photos'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = Column(types.Integer, primary_key=True)
    collection_id = Column(None, ForeignKey('collections.id'), nullable=False)

    name = Column(types.String(255), nullable=False)
    alt = Column(types.Unicode(255), nullable=False, default=u'')
    title = Column(types.Unicode(255), nullable=False, default=u'')
    location = Column(types.Unicode(255), nullable=False, default=u'')
    sequence = Column(types.Integer, nullable=False)

    camera = Column(types.Unicode(255), nullable=True)
    lens = Column(types.Unicode(255), nullable=True)
    aperture = Column(types.Float, nullable=True)
    shutter_speed = Column(types.Float, nullable=False)
    iso = Column(types.Integer, nullable=True)

    width = Column(types.Integer, nullable=False)
    height = Column(types.Integer, nullable=False)
    aspect_ratio = Column(types.Float, nullable=False)

    background_color = Column(types.String(6), nullable=False,
                              default='ffffff')
    perfect_background = Column(types.Boolean, nullable=False, default=False)

    collection = orm.relationship('Collection', backref='photos')

    @staticmethod
    def parse_exif_fraction(val):
        val = str(val)
        if '/' in val:
            a, b = val.split('/')
            val = float(a) / float(b)
        else:
            val = float(val)
        return val

    @classmethod
    def from_file(cls, f, **kwargs):
        tags = exifread.process_file(f)
        im = Image.open(f)

        width, height = im.size
        aspect = float(width) / float(height)
        kwargs.setdefault('width', width)
        kwargs.setdefault('height', height)
        kwargs.setdefault('aspect_ratio', aspect)

        if is_white_background(im):
            kwargs.setdefault('background_color', 'ffffff')
            kwargs.setdefault('perfect_background', True)
        else:
            kwargs.setdefault('background_color', '000000')
            kwargs.setdefault('perfect_background', False)

        camera = tags.get('Image Model')
        if camera:
            kwargs.setdefault('camera', camera)

        lens = tags.get('EXIF LensModel')
        if lens:
            kwargs.setdefault('lens', lens)

        iso = tags.get('EXIF ISOSpeedRatings')
        if iso:
            iso = int(str(iso))
            kwargs.setdefault('iso', iso)

        aperture = tags.get('EXIF FNumber')
        if aperture:
            kwargs.setdefault('aperture', cls.parse_exif_fraction(aperture))

        shutter = tags.get('EXIF ExposureTime')
        if shutter:
            kwargs.setdefault('shutter_speed',
                              cls.parse_exif_fraction(shutter))

        return cls(**kwargs)
