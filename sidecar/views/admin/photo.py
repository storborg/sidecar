from datetime import date

from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from pyramid.view import view_config
from formencode import Schema, validators
from pyramid_uniform import Form, FormRenderer

from ... import model


class PhotoSchema(Schema):
    allow_extra_fields = False
    title = validators.UnicodeString(strip=True, not_empty=True, max=255)


class PhotoHandler(object):
    def __init__(self, request):
        self.request = request

    def _load_object(self):
        request = self.request
        id = request.matchdict['id']
        photo = model.Session.query(model.Photo).get(id)
        if not photo:
            raise HTTPNotFound()
        return photo

    @view_config(route_name='admin_photo',
                 renderer='admin/photo.html',
                 match_param='action=edit')
    def edit(self):
        request = self.request
        photo = self._load_object()

        form = Form(request, PhotoSchema, photo)
        if form.validate():
            # Update item.
            pass

        return dict(photo=photo, renderer=FormRenderer(form))

    @view_config(route_name='admin_photo', match_param='action=delete')
    def delete(self):
        photo = self._load_object()
        model.Session.delete(photo)
        raise HTTPFound(location=request.route_url('admin_collections'))


def includeme(config):
    config.add_route('admin_photo', '/photo/{action}/{id}')
