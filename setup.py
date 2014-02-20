# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='easyurl',
    version='0.0.2',
    description='Easy handling of URLs',
    long_description=readme,
    author='Sergey Panfilov',
    author_email='sergray@gmail.com',
    url='https://github.com/sergray/EasyURL',
    license=license,
    py_modules=['easyurl'],
)
