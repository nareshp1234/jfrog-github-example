#!/usr/bin/env python

from setuptools import setup

setup(
    name='jfrog-python-example',
    version='1.0',
    description='Project example for building Python project with JFrog products',
    author='JFrog',
    author_email='jfrog@jfrog.com',
    url='https://github.com/carmithersh/carmit-testing',
    packages=['pythonExample'],
    install_requires=['PyYAML==3.11', 'nltk','paramiko==1.17.5', 'urllib3==1.25.2','redis == 4.6.0','Flask==2.3.2','gunicorn==22.0.0'],
)
