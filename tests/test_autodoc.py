# -*- coding: utf-8 -*-
"""
    autodoc.tests.test_autodoc
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for Autodoc.


    :copyright: (c) 2014-2018 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
import shutil
from unittest import TestCase
from webtest import TestApp
from autodoc import autodoc
from autodoc._compat import iteritems
from tests.app import create_app

root_path = os.path.dirname(os.path.abspath(__file__))
var_path = os.path.join(root_path, 'var')

os.environ['PYAUTODOC'] = '1'


def clear_generated_file(var_path):
    if os.path.exists(var_path):
        shutil.rmtree(var_path)
        os.mkdir(var_path)
        with open('{0}/.gitkeep'.format(var_path), 'w') as f:
            f.write('')


class TestAutodoc(TestCase):
    def setUp(self):
        app = create_app
        self.client = TestApp(app)

        self.root_path = root_path
        clear_generated_file(var_path)

    def test_parse_response(self):
        """ Should parse WebTest response. """
        res = self.client.post_json('/', params={'message': 'foo'})
        autodoc.parse('POST /', res)

        var = {
            'describe': 'POST /',
            'describe_separators': '======',
            'target_url': 'http://localhost:80',
            'status_code': 200,
            'request': 'POST /',
            'response_body': '{\n  "response": "create"\n}',
            'response_content_type': 'application/json',
            'params': '{\n  "message": "foo"\n}'
        }
        for k, v in iteritems(autodoc.vars[0]):
            self.assertEqual(v, var[k])

        autodoc.clear()

    def test_parse_responses(self):
        """ Should stack responses. """
        res = self.client.get('/')
        autodoc.parse('GET /', res)
        autodoc.parse('GET /', res)
        var = {
            'response_content_type': 'application/json',
            'response_body': '{\n  "response": "index"\n}',
            'describe': 'GET /',
            'request': 'GET /',
            'params': '',
            'status_code': 200,
            'target_url': 'http://localhost:80',
            'describe_separators': '====='
        }
        vars = [var, var]
        self.assertEqual(autodoc.vars, vars)
        autodoc.clear()

    def test_clear_responses(self):
        """ Should clear stacked WebTest responses. """
        res = self.client.get('/')
        autodoc.parse('GET /', res)
        autodoc.parse('GET /', res)
        autodoc.clear()
        self.assertEqual(autodoc.vars, [])

    def test_create_document(self):
        """ Should create reST document. """
        res = self.client.get('/')
        autodoc.parse('GET /', res)
        autodoc.create_document(os.path.join(self.root_path,
                                             'var/test_autodoc.rst'))
        self.assertTrue(os.path.exists(os.path.join(self.root_path,
                                                    'var/test_autodoc.rst')))
        autodoc.clear()

    def test_create_markdown_document(self):
        """ Should create markdown document. """
        res = self.client.get('/')
        autodoc.parse('GET /', res)
        autodoc.template_path = os.path.join(self.root_path,
                                             'templates/markdown.md')
        output = os.path.join(self.root_path, 'var/test_autodoc.md')
        autodoc.create_document(output)
        ret = os.path.exists(output)
        self.assertTrue(ret)
        autodoc.clear()

    def test_should_change_separators(self):
        """ Should change separators. """
        res = self.client.get('/')
        autodoc.separators = '*'
        autodoc.parse('GET /', res)
        var = {
            'response_content_type': 'application/json',
            'response_body': '{\n  "response": "index"\n}',
            'describe': 'GET /',
            'request': 'GET /',
            'params': '',
            'status_code': 200,
            'target_url': 'http://localhost:80',
            'describe_separators': '*****'
        }
        for k, v in iteritems(autodoc.vars[0]):
            self.assertEqual(v, var[k])

        autodoc.clear()


class TestWebTestResponse(TestCase):
    def _getTarget(self):
        from autodoc import WebTestResponse

        return WebTestResponse

    def setUp(self):
        app = create_app
        self.client = TestApp(app)

        clear_generated_file(var_path)

    def test_should_parse_get_request_result(self):
        """ Should parse WebTest GET response. """
        WebTestResponse = self._getTarget()
        res = self.client.get('/')
        ret = WebTestResponse().parse(res)
        var = {
            'status_code': 200,
            'response_body': '{\n  "response": "index"\n}',
            'response_content_type': 'application/json',
            'request': 'GET /',
            'params': '',
            'target_url': 'http://localhost:80'
        }
        self.assertEqual(ret, var)

    def test_should_parse_post_request_result(self):
        """ Should parse WebTest POST response. """
        WebTestResponse = self._getTarget()
        res = self.client.post_json('/', params={'message': 'foo'})
        ret = WebTestResponse().parse(res)
        var = {
            'target_url': 'http://localhost:80',
            'status_code': 200,
            'request': 'POST /',
            'response_body': '{\n  "response": "create"\n}',
            'response_content_type': 'application/json',
            'params': '{\n  "message": "foo"\n}'
        }
        self.assertEqual(ret, var)
