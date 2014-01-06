from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy.orm.exc import NoResultFound

from ..model import Session, Collection, Tag, Photo


def tag_view(request):
    tag_name = request.path_info.lstrip('/')
    try:
        tag = Session.query(Tag).\
            filter_by(name=tag_name).\
            one()
    except NoResultFound:
        raise HTTPNotFound()

    collections = Session.query(Collection).\
        filter(Collection.tags.contains(tag)).\
        filter_by(published=True, listed=True)

    photo_name = request.registry.settings.get('sidecar.photo.%s' % tag_name)
    if photo_name:
        im = Session.query(Photo).\
            filter_by(name=photo_name).\
            one()
    else:
        im = None

    return dict(tag=tag,
                collections=collections,
                panorama=im)
