# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from setuptools import find_packages
from setuptools import setup

from autojump import version


setup(
    name='autojump',
    version=str(version),
    description='Command line utility for easy directory naviation.',
    author='William Ting',
    author_email='io at williamting.com',
    url='https://github.com/wting/autojump/',
    packages=find_packages(exclude=['tests']),
    setup_requires=['setuptools'],
    install_requires=[],
    license='GPL v3',
)
