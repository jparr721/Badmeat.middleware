import os
from setuptools import setup

def read(filename):
	return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
	name='Zeus',
	version='1.0.0',
	author='Jarred Parr',
	scripts=['bin/zeus'],
	author_email='jparr721@gmail.com',
	description='Simple receipt data management',
	license='MIT',
	long_description=read('README.md'),
     )