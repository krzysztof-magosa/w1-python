#!/usr/bin/env python

import pip.download
from pip.req import parse_requirements
from setuptools import setup

setup(
    name='w1',
    version='0.3.0',
    description='Python wrapper for 1-wire Linux interface',
    url='https://github.com/krzysztof-magosa/w1-python',
    author='Krzysztof Magosa',
    author_email='krzysztof@magosa.pl',
    license='MIT',
    packages=[
        'w1'
    ],
    scripts=[
        "bin/w1-therm",
        "bin/w1-api"
    ],
    install_requires=[]
)
