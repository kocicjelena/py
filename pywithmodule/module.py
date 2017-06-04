#!/usr/bin/env python
import os
import re
import sys

from setuptools import find_packages, setup
def main ():
    try:
        root = __file__
        if os.path.islink (root):
            root = os.path.realpath (root)
        return os.path.dirname (os.path.abspath (root))
    except:
        print "no root"
        sys.exit ()
     
def start ():
    print "module is ready to be implemented"
    print determine_path ()
    print "My django blog module is in:"
    files = [f for f in os.listdir(determine_path () + "/Blog/*")]
    print files
    
if __name__ == "__main__":
    //print "please integrate"
    os.system('python manage.py runserver')
