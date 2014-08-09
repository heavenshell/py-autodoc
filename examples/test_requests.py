# -*- coding: utf-8 -*-
"""
    autodoc.tests.test_requests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Autodoc for UnitTest.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
from unittest import TestCase
from mock import patch
from requests import Request, Session, Response
from autodoc import autodoc
from autodoc._compat import urlencode

def dummy_response(m, request, params, filename=None):
    response = Response()
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json'
    response.request = request
    response.request.body = urlencode(params)
    response.request.path_url = '/'
    if filename is None:
        response._content = ''
    else:
        root_path = os.path.dirname(os.path.abspath(__file__))
        file_path = root_path + '/' + filename
        with open(file_path, 'r') as f:
            data = f.read()
            response._content = data

    m.return_value = response


class TestUnittest(TestCase):
    def create_request(self, url, method, data=None):
        headers = {'content-type': 'application/json'}
        request = Request(method, url, data=data, headers=headers)

        return request

    @patch('requests.sessions.Session.send')
    def send(self, request, params, file_path, m):
        dummy_response(m, request, params, file_path)

        session = Session()
        res = session.send(request.prepare())

        return res

    @classmethod
    @autodoc.generate('var/test_requests.rst')
    def tearDownClass(cls):
        pass

    @autodoc.describe('GET /')
    def test_get(self):
        """ GET / """
        req = self.create_request('http://localhost:5000/', 'GET')
        res = self.send(req, '', '../tests/data/get.json')
        self.assertEqual(res.status_code, 200)

        return res

    @autodoc.describe('POST /')
    def test_post(self):
        """ POST / """
        params = {'id': 1, 'message': 'foo'}
        req = self.create_request('http://localhost:5000/', 'POST', params)
        res = self.send(req, params, '../tests/data/post.json')

        self.assertEqual(res.status_code, 200)

        return res

    @autodoc.describe('POST /foo/bar')
    def test_foo_bar(self):
        """ POST /foo/bar """
        params = {'id': 1, 'message': 'foo'}
        req = self.create_request('http://localhost:5000/foo/bar', 'POST',
                                  params)
        res = self.send(req, params, '../tests/data/post.json')
        self.assertEqual(res.status_code, 200)

        return res
