#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://aviio_technical_component.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='aviio_technical_component',
    version='0.1.0',
    description='Consume API endpoint, handle errors, structure data to csv',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Christine K. Rogers',
    author_email='rogersckw@gmail.com',
    url='https://github.com/ckrogers/aviio_technical_component',
    packages=[
        'aviio_technical_component',
    ],
    package_dir={'aviio_technical_component': 'aviio_technical_component'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='aviio_technical_component',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
