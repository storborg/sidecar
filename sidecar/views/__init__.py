import os
import os.path


__here__ = os.path.abspath(os.path.dirname(__file__))
repo_base = os.path.dirname(os.path.dirname(os.path.dirname(__here__)))


def includeme(config):
    #config.include('.admin', route_prefix='a')

    config.add_route('index', '/')
    config.add_view('.index.index_view', route_name='index',
                    renderer='tag.html')

    config.add_route('all', '/all')
    config.add_view('.index.all_view', route_name='all',
                    renderer='tag.html')

    tags = config.registry.settings.get('sidecar.header_tags', '')
    for tag in tags.split():
        config.add_route(tag, tag)
        config.add_view('.tag.tag_view', route_name=tag, renderer='tag.html')

    config.add_route('about', '/about')
    config.add_view('.about.about_view', route_name='about',
                    renderer='about.html')

    config.add_route('photo', '/photo/{id}')
    config.add_view('.photo.photo_view', route_name='photo',
                    renderer='photo.html')

    config.add_route('collection', '/*path')
    config.add_view('.collection.collection_view', route_name='collection',
                    renderer='collection.html')

    config.include('.error')
