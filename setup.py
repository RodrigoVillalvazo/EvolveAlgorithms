#!/usr/bin/env python

from distutils.core import setup
import setuptools

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

setup(name="EvolveAlgorithms", 
      version='1.0',
      description='Evolve algorithms for robotics',
      author='Rodrigo Villalvazo',
      author_email='rodri.villalvazo3@gmail.com',
      install_requires=load_requirements("requirements.txt"))
