# -*- coding: utf-8 -*-
"""
    Add comment here
    ~~~~~~~~~~~~~~~~

    Add descripton here


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import shutil
import requests
from urllib.parse import urlencode
from requests import Request, Session
from unittest import TestCase
from mock import patch
from autodoc import autodoc
from autodoc._compat import iteritems

root_path = os.path.dirname(os.path.abspath(__file__))
var_path = os.path.join(root_path, 'var')

os.environ['PYAUTODOC'] = '1'


def dummy_response(m, request, params, filename=None):
    response = requests.Response()
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

    def setUp(self):
        self.client = requests
        self.root_path = root_path
        if os.path.exists(var_path):
            shutil.rmtree(var_path)
            os.mkdir(var_path)

    @patch('requests.sessions.Session.send')
    def test_parse_response(self, m):
        """ Should parse requests response. """
        params = {'message': 'foo'}
        headers = {'content-type': 'application/json'}
        req = self.create_request('http://localhost:5000/', 'POST', data=params,
                                  headers=headers)
        dummy_response(m, req, params, 'data/post.json')


        session = Session()
        res = session.send(req.prepare())

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
