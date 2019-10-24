#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-
"""
setup.py script for the ParcourSup.py project (https://github.com/Naereen/ParcourSup.py)

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
long_description = "test-of-airspeed-velocity"


version = "0.0.1"


setup(name="test-of-airspeed-velocity",
    version=version,
    description="test-of-airspeed-velocity",
    long_description=long_description,
    author="Lilian Besson",
    author_email="naereen AT crans DOT org".replace(" AT ", "@").replace(" DOT ", "."),
    url="https://github.com/Naereen/test-of-airspeed-velocity",
    download_url="https://github.com/Naereen/test-of-airspeed-velocityreleases/",
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
        "SMPyBandits",
    ],
    package_data={
    },
    # project_urls={  # Optional
    #     "Bug Reports": "https://github.com/Naereen/test-of-airspeed-velocityissues",
    #     "Source":      "https://github.com/Naereen/test-of-airspeed-velocitytree/master/",
    # },
)

# End of setup.py
