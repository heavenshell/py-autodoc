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
from unittest import TestCase
from webtest import TestApp
from autodoc import autodoc
from tests.app import create_app


root_path = os.path.dirname(os.path.abspath(__file__))
var_path = os.path.join(root_path, 'var')

os.environ['PYAUTODOC'] = '1'


class TestAutodocGenerate(TestCase):
    def setUp(self):
        app = create_app
        self.client = TestApp(app)

        if os.path.exists(var_path):
            shutil.rmtree(var_path)
            os.mkdir(var_path)

    @classmethod
    @autodoc.generate(
        os.path.join(var_path, 'test_generate.md'),
        template=os.path.join(root_path, 'templates/markdown.md'))
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


class TestGenerated(TestCase):
    def test_generate(self):
        """ Document file should generated. """
        ret = os.path.exists(os.path.join(var_path, 'test_generate.md'))
        self.assertTrue(ret)
