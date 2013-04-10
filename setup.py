#!/usr/bin/env python

from setuptools import setup
from subprocess import call

def convert_readme():
    try:
        call(["pandoc", "-t",  "rst", "-o",  "README.txt", "readme.md"])
    except OSError:
        pass
    return open('README.txt').read()

setup(name='mongodeform',
    version='0.1',
    description="An implementation of deform using mongoengine. Based on django-mongodbforms.",
    author='Ivan Miric',
    author_email='imiric@gmail.com',
    url='https://github.com/imiric/mongodeform',
    packages=['mongodeform',],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    license='New BSD License',
    long_description=convert_readme(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools', 'deform>=0.9.7', 'mongoengine>=0.6',],
)
