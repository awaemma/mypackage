from setuptools import setup, find_packages

setup(
name='myPackage',
version='0.1',
packages=find_packages(exclude=['tests*']),
license='MIT',
description= 'EDSA example python package',
long_description=open('readme.MD').read(),
install_requires= ['numpy'],
author='Kings Gig'

)