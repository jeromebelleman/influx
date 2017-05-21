#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='influx',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Query InfluxDB",
    long_description="Query InfluxDB with some useful tricks.",
    scripts=['influx'],
    data_files=[('share/man/man1', ['influx.1'])],
)
