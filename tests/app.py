# -*- coding: utf-8 -*-
"""
    autodoc.tests.app
    ~~~~~~~~~~~~~~~~~

    Dummy application.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import json
from autodoc._compat import PY2


def index():
    return json.dumps({'response': 'index'})


def create():
    return json.dumps({'response': 'create'})


def update():
    return json.dumps({'response': 'update'})


def delete():
    return json.dumps({'response': 'delete'})


def foo_bar():
    return json.dumps({'response': 'foo_bar'})


def create_response(patterns, environ):
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    for p in patterns:
        if path == p['route'] and method == p['method']:
            return p['view']()


def create_app(environ, start_response):
    routes = [
        {'route': '/', 'view': index, 'method': 'GET'},
        {'route': '/', 'view': create, 'method': 'POST'},
        {'route': '/', 'view': update, 'method': 'PUT'},
        {'route': '/', 'view': delete, 'method': 'DELETE'},
        {'route': '/foo/bar', 'view': foo_bar, 'method': 'POST'}
    ]

    response = create_response(routes, environ)
    if not PY2:
        response = bytes(response, 'utf-8')

    headers = [('Content-Type', 'application/json'),
               ('Content-Length', str(len(response)))]
    start_response('200 Ok', headers)

    return [response]
