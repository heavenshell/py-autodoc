# -*- coding: utf-8 -*-
"""
    autodoc.compat
    ~~~~~~~~~~~~~~

    Compatible to Python2.6,2.7 and Python3.3

    This module is copyed from Werkzeug's `_compat.py`.

    https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/_compat.py

    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import sys

PY2 = sys.version_info[0] == 2


if PY2:
    from urlparse import parse_qsl as parse_qsl
    from urllib import urlencode as urlencode
    text_type = unicode

    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()
else:
    from urllib.parse import parse_qsl as parse_qsl
    from urllib.parse import urlencode as urlencode
    text_type = str

    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())


def to_unicode(x, charset=sys.getdefaultencoding(), errors='strict',
               allow_none_charset=False):
    if x is None:
        return None
    if not isinstance(x, bytes):
        return text_type(x)
    if charset is None and allow_none_charset:
        return x
    return x.decode(charset, errors)
