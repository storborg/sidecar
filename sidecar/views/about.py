from ..model import Session, Collection


def about_view(request):
    collection = Session.query(Collection).\
        filter_by(path='about').\
        one()
    return dict(collection=collection)
