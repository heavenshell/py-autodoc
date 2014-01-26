# -*- coding: utf-8 -*-
"""
    Autodoc
    ~~~~~~~

    Autodoc Python implementation.


    `Ruby autodoc <https://github.com/r7kamura/autodoc>`_
    `Perl autodoc <https://metacpan.org/pod/Test::JsonAPI::Autodoc>`_


    :copyright: (c) 2014 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import os
from setuptools import setup, find_packages

requires = ['webtest', 'decorator']
try:
    import argparse
except:
    requires.append('argparse')

app_name = 'autodoc'

rst_path = os.path.join(os.path.dirname(__file__), 'README.rst')
description = ''
with open(rst_path) as f:
    description = f.read()

setup(
    name=app_name,
    version='0.2',
    author='Shinya Ohyanagi',
    author_email='sohyanagi@gmail.com',
    url='http://github.com/heavenshell/py-autodoc',
    description='Autodoc Python implementation.',
    long_description=description,
    license='BSD',
    platforms='any',
    packages=find_packages(exclude=['tests']),
    package_dir={'': '.'},
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Testing'
    ],
    tests_require=['webtest'],
    test_suite='tests'
)
