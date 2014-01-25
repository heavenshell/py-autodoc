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


class TestAutodocNotGenerate(TestCase):
    def setUp(self):
        app = create_app
        self.client = TestApp(app)

        if os.path.exists(var_path):
            shutil.rmtree(var_path)
            os.mkdir(var_path)

    @staticmethod
    @autodoc.generate(
        os.path.join(var_path, 'test_generate.md'),
        template=os.path.join(root_path, 'templates/markdown.md'))
    def tearDownClass(cls):
        pass
        ret = os.path.exists(os.path.join(var_path, 'test_generate.md'))
        assert ret is False

    @autodoc.describe('GET /')
    def test_should_not_generate(self):
        """ Should not generate when PYAUTODOC environ is not exists. """
        del os.environ['PYAUTODOC']

        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

        return res


class TestNotGenerate(TestCase):
    def test_not_generated(self):
        """ Document file should not generated. """
        ret = os.path.exists(os.path.join(var_path, 'test_generate.md'))
        self.assertFalse(ret)
