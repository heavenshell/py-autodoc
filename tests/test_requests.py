# -*- coding: utf-8 -*-
"""
    autodoc.tests.test_requests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for `requests` client.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import shutil
from urllib.parse import urlencode
from requests import Request, Session, Response
from unittest import TestCase
from mock import patch
from autodoc import autodoc
from autodoc._compat import iteritems

root_path = os.path.dirname(os.path.abspath(__file__))
var_path = os.path.join(root_path, 'var')

os.environ['PYAUTODOC'] = '1'


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


class TestRequestsResponse(TestCase):
    def create_request(self, url, method, data=None, headers=None):
        request = Request(method, url, data=data, headers=headers)

        return request

    @patch('requests.sessions.Session.send')
    def send(self, request, params, file_path, m):
        dummy_response(m, request, params, file_path)

        session = Session()
        res = session.send(request.prepare())

        return res

    def setUp(self):
        self.root_path = root_path
        if os.path.exists(var_path):
            shutil.rmtree(var_path)
            os.mkdir(var_path)

    def test_parse_response(self):
        """ Should parse requests response. """
        params = {'message': 'foo'}
        headers = {'content-type': 'application/json'}
        req = self.create_request(url='http://localhost:5000/',
                                  method='POST',
                                  data=params,
                                  headers=headers)

        res = self.send(req, params, 'data/post.json')
        autodoc.parse('POST /', res)

        var = {
            'describe': 'POST /',
            'describe_separators': '======',
            'target_url': 'http://localhost:5000/',
            'status_code': 200,
            'request': 'POST /',
            'response_body': '{"response": "create"}\n',
            'response_content_type': 'application/json',
            'params': '{\n  "message": "foo"\n}'
        }
        for k, v in iteritems(autodoc.vars[0]):
            self.assertEqual(v, var[k])

        autodoc.clear()

    def test_parse_responses(self):
        """ Should stack responses. """
        headers = {'content-type': 'application/json'}
        req = self.create_request(url='http://localhost:5000/',
                                  method='GET',
                                  headers=headers)

        res = self.send(req, '', 'data/get.json')
        autodoc.parse('GET /', res)
        autodoc.parse('GET /', res)
        var = {
            'response_content_type': 'application/json',
            'response_body': '{"response": "index"}\n',
            'describe': 'GET /',
            'request': 'GET /',
            'params': {},
            'status_code': 200,
            'target_url': 'http://localhost:5000/',
            'describe_separators': '====='
        }
        vars = [var, var]
        self.assertEqual(autodoc.vars, vars)
        autodoc.clear()

    def test_clear_responses(self):
        """ Should clear stacked WebTest responses. """
        headers = {'content-type': 'application/json'}
        req = self.create_request(url='http://localhost:5000/',
                                  method='GET',
                                  headers=headers)

        res = self.send(req, '', 'data/get.json')

        autodoc.parse('GET /', res)
        autodoc.parse('GET /', res)
        autodoc.clear()
        self.assertEqual(autodoc.vars, [])
