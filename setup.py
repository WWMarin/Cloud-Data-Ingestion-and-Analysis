# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Cloud Data Ingestion and Analysis',
    version='0.1.0',
    description='An example project of a data ingestion using a cloud service and data analysis scripts',
    long_description=readme,
    author='Werner W. Marin',
    author_email='wernermarin@gmail.com',
    url='https://github.com/WWMarin/Cloud-Data-Ingestion-and-Analysis',
    license=license,
    packages=find_packages()
)