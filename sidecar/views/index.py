from ..model import Session, Collection, Photo


def index_view(request):
    collections = Session.query(Collection).\
        filter_by(published=True, listed=True).\
        limit(4)
    name = request.registry.settings.get('sidecar.photo.index')
    if name:
        im = Session.query(Photo).\
            filter_by(name=name).\
            one()
    else:
        im = None
    return dict(collections=collections,
                panorama=im)


def all_view(request):
    collections = Session.query(Collection).\
        filter_by(published=True, listed=True)
    name = request.registry.settings.get('sidecar.photo.all')
    if name:
        im = Session.query(Photo).\
            filter_by(name=name).\
            one()
    else:
        im = None
    return dict(collections=collections,
                panorama=im)
