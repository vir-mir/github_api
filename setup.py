#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import api_github

setup(
    name='api_github',
    version=api_github.version,
    packages=find_packages(),
    install_requires='requests',
    url='https://github.com/vir-mir/github_api',
    license='MIT',
    author='vir-mir',
    keywords='github.com github api',
    author_email='virmir49@gmail.com',
    description='agihub.com API Python wrapper',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
