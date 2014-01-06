from datetime import datetime

from sqlalchemy import Table, Column, ForeignKey, types, orm

from webhelpers2.html import literal
from markdown import markdown

from .imageset import ImageSetExtension

from .base import Base


collection_tags = Table(
    'collection_tags',
    Base.metadata,
    Column('collection_id', None, ForeignKey('collections.id'),
           primary_key=True),
    Column('tag_id', None, ForeignKey('tags.id'), primary_key=True),
    mysql_engine='InnoDB')


class Collection(Base):
    __tablename__ = 'collections'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = Column(types.Integer, primary_key=True)
    path = Column(types.String(255), nullable=True)
    external_url = Column(types.String(255), nullable=True)
    title = Column(types.Unicode(255), nullable=False)
    teaser = Column(types.UnicodeText, nullable=False, default=u'')
    body = Column(types.UnicodeText, nullable=False, default=u'')
    body_format = Column(types.String(4), nullable=False, default=u'md')
    published = Column(types.Boolean, nullable=False, default=False)
    listed = Column(types.Boolean, nullable=False, default=False)
    show_gallery = Column(types.Boolean, nullable=False, default=True)
    publish_date = Column(types.DateTime, nullable=False,
                          default=datetime.now)

    tags = orm.relationship('Tag', backref='collections',
                            collection_class=set,
                            secondary=collection_tags)

    def render_body(self, request):
        if self.body_format == 'html':
            return literal(self.body)
        elif self.body_format == 'md':
            photos = self.photos
            return literal(markdown(
                self.body,
                extensions=[ImageSetExtension(request, photos)]))
        else:
            return self.body
