#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


setup(
    name='rst2accounts',
    version='1.0.0',
    description='Calculate totals per operations in your ReST table accounts.',
    long_description=open('README.rst').read(),
    author=u'François Magimel',
    author_email='francois.magimel@perdu.fr',
    url='https://github.com/Linkid/rst2accounts',
    license='BSD',
    packages=find_packages(exclude=['tests']),
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
    entry_points={
        'console_scripts': [
            'rst2accounts=rst2accounts.main:main',
        ],
    },
)
