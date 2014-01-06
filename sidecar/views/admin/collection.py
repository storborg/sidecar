from datetime import date

from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config
from formencode import Schema, validators
from pyramid_uniform import Form, FormRenderer

from ... import model


class CollectionSchema(Schema):
    allow_extra_fields = False
    title = validators.UnicodeString(strip=True, not_empty=True, max=255)
    external_url = validators.String(strip=True, max=255)
    path = validators.String(strip=True, max=255)
    teaser = validators.UnicodeString()
    publish_date = validators.String()
    published = validators.Bool()
    listed = validators.Bool()
    show_gallery = validators.Bool()
    body_format = validators.OneOf(['md', 'html'])
    body = validators.UnicodeString()


class CollectionHandler(object):
    def __init__(self, request):
        self.request = request

    def _load_object(self):
        request = self.request
        id = request.matchdict['id']
        collection = model.Session.query(model.Collection).get(id)
        if not collection:
            raise HTTPNotFound()
        return collection

    @view_config(route_name='admin_collection',
                 renderer='admin/collection.html',
                 match_param='action=edit')
    def edit(self):
        request = self.request
        collection = self._load_object()

        form = Form(request, CollectionSchema)
        if form.validate(skip_csrf=True):
            # Update item.
            form.bind(collection)

        return dict(collection=collection, renderer=FormRenderer(form))

    @view_config(route_name='admin_collections',
                 renderer='admin/collections.html')
    def index(self):
        request = self.request
        if request.method == 'POST':
            today = date.today()
            collection = model.Collection(title=u'New Collection - %s' % today)
            model.Session.add(collection)
            model.Session.flush()
            return HTTPFound(location=request.route_url('admin_collection',
                                                        action='edit',
                                                        id=collection.id))

        collections = model.Session.query(model.Collection).\
            order_by(model.Collection.id.desc())
        return dict(collections=collections)

    @view_config(route_name='admin_collection', match_param='action=delete')
    def delete(self):
        request = self.request
        collection = self._load_object()
        model.Session.delete(collection)
        raise HTTPFound(location=request.route_url('admin_collections'))


def includeme(config):
    config.add_route('admin_collections', '/collections')
    config.add_route('admin_collection', '/collection/{action}/{id}')
