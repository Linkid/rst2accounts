#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


setup(
    name='rst2accounts',
    version='0.1',
    description='Complete your accounts in ReST',
    long_description=open('README.rst').read(),
    author=u'François Magimel',
    url='https://github.com/Linkid/rst2accounts',
    license='BSD',
    packages=find_packages(),
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent"
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
    ],
)
