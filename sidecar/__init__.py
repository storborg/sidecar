from pyramid.config import Configurator
from pyramid.events import BeforeRender
from sqlalchemy import engine_from_config

from . import helpers
from .model import Session, Base


def add_renderer_globals(event):
    event['h'] = helpers


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    Session.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)

    config.include('.themes')
    config.include('.views')

    config.add_subscriber(add_renderer_globals, BeforeRender)
    #config.scan()

    return config.make_wsgi_app()
