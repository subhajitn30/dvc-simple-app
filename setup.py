### Create the package by using setup tools
## To create the packages 

from setuptools import setup, find_packages, version ## it will find all the dependent packages

setup(
    
    name='src',
    version='0.0.1',
    description="It's a wine package",
    author="subhajit",
    packages = find_packages(),
    license="MIT"

)