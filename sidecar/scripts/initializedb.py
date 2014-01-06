import os
import sys
import transaction

from sqlalchemy import engine_from_config
from pyramid.paster import get_appsettings, setup_logging

from ..model import Session, Base, Collection


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)

    engine = engine_from_config(settings, 'sqlalchemy.')
    Session.configure(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        collection = Collection(
            title=u'Welcome to Sidecar',
            path='welcome',
            teaser=(u'Sidecar is a simple site publishing platform for '
                    u'photographers. This is a sample collection to get '
                    u'you started.'),
            published=True,
            listed=True)
        Session.add(collection)
