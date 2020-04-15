from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
from setuptools import setup
setup(name='dsp_py',
version='0.0.4',
description='A support library for Digital Signal Processing',
url='https://github.com/dinhanhx/DSP-py-lib',
author='dinhanhx',
author_email='dinhanhx@gmail.com',
license='The Unlicensed',
packages=['dsp_py'],
zip_safe=False,
install_requires=['numpy', 'scipy', 'matplotlib', 'colorama'])
