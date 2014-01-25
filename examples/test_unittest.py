# -*- coding: utf-8 -*-
"""
    autodoc.tests.test_unittest
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Autodoc for UnitTest.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
from unittest import TestCase
from webtest import TestApp
from autodoc import autodoc
from tests.app import create_app


class TestUnittest(TestCase):
    def setUp(self):
        app = create_app
        self.client = TestApp(app)

    @classmethod
    @autodoc.generate('var/test_unittest.rst')
    def tearDownClass(cls):
        pass

    @autodoc.describe('GET /')
    def test_get(self):
        """ GET / """
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

        return res

    @autodoc.describe('POST /')
    def test_post(self):
        """ POST / """
        res = self.client.post_json('/', params={'id': 1, 'message': 'foo'})
        self.assertEqual(res.status_code, 200)

        return res

    @autodoc.describe('POST /foo/bar')
    def test_foo_bar(self):
        """ POST /foo/bar """
        res = self.client.post_json('/foo/bar', params={'id': 1, 'message': 'foo'})
        self.assertEqual(res.status_code, 200)

        return res
