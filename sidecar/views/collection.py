from sqlalchemy.orm.exc import NoResultFound
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

from ..model import Session, Collection


def collection_view(request):
    path = '/'.join(request.matchdict['path'])
    try:
        collection = Session.query(Collection).\
            filter_by(path=path, published=True).\
            one()
    except NoResultFound:
        raise HTTPNotFound()
    if collection.external_url:
        raise HTTPFound(location=collection.external_url)
    photos = collection.photos
    return dict(collection=collection,
                photos=photos)
