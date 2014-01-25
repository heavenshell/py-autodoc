# -*- coding: utf-8 -*-
"""
    autodoc.tests.tests_pytest
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Autodoc for PyTest.


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import sys
from webtest import TestApp
from autodoc import autodoc
from tests.app import create_app
try:
    import pytest
except ImportError:
    sys.exit(1)


@pytest.fixture
def setup():
    setup = TestApp(create_app)

    return setup


@autodoc.generate('var/test_pytest.md', template='templates/markdown.md')
def teardown_module(module):
    pass


@autodoc.describe('GET /')
def test_index():
    app = TestApp(create_app)
    res = app.get('/')
    assert res.status_code == 200

    return res


@autodoc.describe('POST /')
def test_post(setup):
    res = setup.post_json('/', params={'id': 1, 'message': 'foo'})
    assert res.status_code == 200

    return res
