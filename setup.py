# -*- coding: utf-8 -*-
import os
import shutil
import zipfile
from pathlib import Path
from setuptools import setup, find_packages


########## PACKAGE INFO ##########
name = 'pyTkTimeGraph'
description='Python implementation of a live plot using tinker'
version ='1.0'
author='iz2k'

try:
  shutil.rmtree(Path('dist'))
except:
  pass
os.mkdir(Path('dist'))

# Read additional files
with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

# Create wheel
setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author=author,
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements
)

try:
  shutil.rmtree(Path(name + '.egg-info'))
except:
  pass
try:
  shutil.rmtree(Path('build'))
except:
  pass
