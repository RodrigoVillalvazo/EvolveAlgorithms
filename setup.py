#!/usr/bin/env python

from distutils.core import setup
import sys
warnings = list()
try:
    from setuptools import setup, Extension, find_packages
    modules = find_packages(exclude=['libs', 'Results', 'Simulations'])
except ImportError:
    warnings.append("warning: using disutils.core.setup, cannot use \"develop\" option")
    from disutils.core import setup, Extension
    modules = ['libs', 'Results', 'Simulations']

from setuptools.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

if sys.platform == 'win32' and sys.version_info > (2, 6):
   # 2.6's distutils.msvc9compiler can raise an IOError when failing to
   # find the compiler
   # It can also raise ValueError http://bugs.python.org/issue7511
   ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError,
                 IOError, ValueError)
else:
   ext_errors = (CCompilerError, DistutilsExecError, DistutilsPlatformError)

class BuildFailed(Exception):
    pass

class ve_build_ext(build_ext):
    # This class allows C extension building to fail.

    def run(self):
        try:
            build_ext.run(self)
        except DistutilsPlatformError as e:
            print(e)
            raise BuildFailed()

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except ext_errors as e:
            print(e)
            raise BuildFailed()
        
def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.requirement) for ir in reqs]

def run_setup():
    setup(
      name="EvolveAlgorithms", 
      version='1.0',
      description='Evolve algorithms for robotics',
      author='Rodrigo Villalvazo',
      author_email='rodri.villalvazo3@gmail.com',
      platforms=['any'],
      packages=find_packages(exclude=['examples']),
      cmdclass={"build_ext": ve_build_ext},
      install_requires=load_requirements("requeriments.txt"))
    

try:
    run_setup()
except BuildFailed:
    print("*" * 75)
    print("WARNING: The C extensions could not be compiled, "
          "speedups won't be available.")
    print("Now building without C extensions.")
    print("*" * 75)

    run_setup()

    print("*" * 75)
    print("WARNING: The C extensions could not be compiled, "
          "speedups won't be available.")
    print("Plain-Python installation succeeded.")
    print("*" * 75)

print("\n".join(warnings))