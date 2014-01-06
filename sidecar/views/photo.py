from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from ..model import Session, Photo


def photo_view(request):
    id = request.matchdict['id']
    try:
        photo = Session.query(Photo).\
            filter_by(id=id).\
            one()
    except NoResultFound:
        raise HTTPNotFound()

    next_photo = Session.query(Photo).\
        filter(Photo.sequence > photo.sequence,
               Photo.collection == photo.collection).\
        order_by(Photo.sequence).\
        first()

    prev_photo = Session.query(Photo).\
        filter(Photo.sequence < photo.sequence,
               Photo.collection == photo.collection).\
        order_by(Photo.sequence.desc()).\
        first()

    return dict(photo=photo,
                next_photo=next_photo,
                prev_photo=prev_photo,
                collection=photo.collection)
