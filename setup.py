import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'pyramid_frontend',
    'pyramid_uniform',
    'zope.sqlalchemy',
    'waitress',
    'exifread',
    'markdown',
    'WebHelpers2',
]

setup(name='sidecar',
      version='0.0',
      description='sidecar',
      long_description='',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Scott Torborg',
      author_email='storborg@gmail.com',
      url='http://www.scotttorborg.com',
      keywords='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='sidecar',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = sidecar:main
      [console_scripts]
      initialize_sidecar_db = sidecar.scripts.initializedb:main
      """,
      )
