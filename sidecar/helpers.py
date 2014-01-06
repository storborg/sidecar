import string
from webhelpers2.constants import *
from webhelpers2.html.tags import *
from webhelpers2.html import *
from webhelpers2.html.tags import _make_safe_id_component
from webhelpers2.text import *
from webhelpers2.date import *


def to_css_color(rgb):
    return 'rgb(%d, %d, %d)' % rgb


def linkify_camera(name):
    name = str(name)
    camera_reviews = {
        #'Canon EOS 5D Mark III': '/canon-5d-mark-3-review',
        'Canon EOS M': '/canon-eos-m-teardown',
    }
    if name in camera_reviews:
        return link_to(name, camera_reviews[name])
    else:
        return name


def linkify_lens(name):
    name = str(name)
    lens_reviews = {
        #'EF35mm f/2 IS USM': '/canon-35mm-f2-is-usm',
    }
    if name in lens_reviews:
        return link_to(name, lens_reviews[name])
    else:
        return name


def format_shutter_speed(shutter_speed):
    """
    Given a float representing seconds, guess at what fraction it is, and
    return a string with the fraction and the float.

    E.g.
    0.00625 -> "0.006 sec (1/160)"
    1.0 -> "1.0 sec"

    """
    if shutter_speed > 1:
        return "%0.1f sec" % shutter_speed
    else:
        return "%0.3f sec (1/%d)" % (shutter_speed, 1.0 / shutter_speed)


def grouper(n, iterable):
    """
    Return elements from iterable n items at a time.
    e.g. grouper(3,[1,2,3,4,5,6,7]) -> ([1,2,3], [4,5,6], [7])
    """
    iterable = iter(iterable)
    ret = []
    for item in iterable:
        ret.append(item)
        if len(ret) >= n:
            yield ret
            ret = []
    if len(ret) > 0:
        yield ret


def prettify(name):
    """
    Take a string (or something that can be made into a string), replace
    underscores with spaces, and capitalize the first letter.

    >>> prettify("joe_user")
    'Joe user'
    >>> prettify("foo_bar_baz_quux")
    'Foo bar baz quux'
    >>> prettify(123)
    '123'
    """
    return str(name).replace('_', ' ').capitalize()
