#!/usr/bin/python
import os
import sys
from io import open
from setuptools import setup
from distutils.core import setup

files = ["Blog/*", "Template/*", "static/*"]

venv = os.path.join('<venv>', '/Scripts/activate.bat')
rr = os.path.join('venv', 'mysite/manage.py')
#execfile(venv, dict(__file__=venv))
#python -c 'import setuptools; execfile(mysite/manage.py)' runserver
#r = os.path.join("python", 'mysite/manage.py', "runserver")
#execfile(venv, dict(__file__=r))
#python -c execfile(virtualenv, dict(__file__=r)) runserver
#python -c "import setuptools; execfile('mysite/manage.py')" runserver
setup(name='pywithmodule',
      packages=['pywithmodule'],
      version='1.4',
      description='dja App',
      author='Jelena',
      author_email='kocicjelena@gmail.com',
	  include_package_data=True,
	  url='https://github.com/kocicjelena/py/',
	  install_requires=['Django<=1.10'],
	  scripts = ["runner"],
	  console_scripts=['pywithmodule.manage:runserver'],
	  
     )
