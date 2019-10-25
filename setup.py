#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-
"""
setup.py script for the SMPyBandits-benchmarks project (https://github.com/Naereen/SMPyBandits-benchmarks)

References:
- https://packaging.python.org/en/latest/distributing/#setup-py
- https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html#setup-py-description
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
long_description = """
Airspeed Velocity benchmarks for SMPyBandits
https://github.com/Naereen/SMPyBandits-benchmarks

This repository contains code (and soon, also results) of benchmarks for the SMPyBandits python package, using the airspeed velocity tool.

This project is written by Lilian Besson's, written in Python (2 or 3), to test the quality of SMPyBandits, my open-source Python package for numerical simulations on slot_machine single-player and multi-players Multi-Armed Bandits (MAB) algorithms.

A complete Sphinx-generated documentation for SMPyBandits is on SMPyBandits.GitHub.io.
"""


version = "0.0.1"


setup(name="SMPyBandits-benchmarks",
    version=version,
    description="SMPyBandits-benchmarks",
    long_description=long_description,
    author="Lilian Besson",
    author_email="naereen AT crans DOT org".replace(" AT ", "@").replace(" DOT ", "."),
    url="https://github.com/Naereen/SMPyBandits-benchmarks",
    download_url="https://github.com/Naereen/SMPyBandits-benchmarksreleases/",
    license="MIT",
    platforms=["GNU/Linux"],
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="open-source",
    # py_modules=["parcoursup"],
    # packages=[
    #     "",
    # ],
    install_requires=[
        "numpy",
        "scipy",
        "tqdm",
        "numba",
        "SMPyBandits>=0.9.7",
    ],
    package_data={
    },
    # project_urls={  # Optional
    #     "Bug Reports": "https://github.com/Naereen/test-of-airspeed-velocityissues",
    #     "Source":      "https://github.com/Naereen/test-of-airspeed-velocitytree/master/",
    # },
)

# End of setup.py
