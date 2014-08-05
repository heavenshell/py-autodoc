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
from unittest import TestCase
from unittest import skip
from autodoc import autodoc
from autodoc._compat import iteritems


root_path = os.path.dirname(os.path.abspath(__file__))
var_path = os.path.join(root_path, 'var')

os.environ['PYAUTODOC'] = '1'


class TestRequestsResponse(TestCase):
    def setUp(self):
        self.client = requests

        self.root_path = root_path
        if os.path.exists(var_path):
            shutil.rmtree(var_path)
            os.mkdir(var_path)

    # TODO Add mock
    @skip('Skip')
    def test_parse_response(self):
        """ Should parse requests response. """
        params = {'message': 'foo'}
        headers = {'content-type': 'application/json'}
        res = self.client.post('http://localhost:5000', data=params,
                               headers=headers)
        autodoc.parse('POST /', res)

        var = {
            'describe': 'POST /',
            'describe_separators': '======',
            'target_url': 'http://localhost:5000/',
            'status_code': 200,
            'request': 'POST /',
            'response_body': '{"response": "create"}',
            'response_content_type': 'application/json',
            'params': '{\n  "message": "foo"\n}'
        }
        for k, v in iteritems(autodoc.vars[0]):
            self.assertEqual(v, var[k])
