# Author: Sobassy <contact@sobassy.jp>
# Copyright (c) 2023-2024 Sobassy
# License: MIT License

from setuptools import setup
import xplane_api

DESCRIPTION = "xplane-api: Python library for getting and manipulating X-Plane values via UDP."
NAME = 'xplane-api'
AUTHOR = 'Sobassy'
AUTHOR_EMAIL = 'contact@sobassy.jp'
URL = 'https://github.com/sobassy/XPlanePythonAPI'
LICENSE = 'MIT License'
DOWNLOAD_URL = 'https://github.com/sobassy/XPlanePythonAPI'
VERSION = xplane_api.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = []

EXTRAS_REQUIRE = {}

PACKAGES = [
    'xplane_api'
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Manufacturing',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Games/Entertainment',
    'Topic :: Games/Entertainment :: Simulation',
]

with open('README.md', 'r') as fp:
    readme = fp.read()

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/markdown",
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=PACKAGES,
    classifiers=CLASSIFIERS
)
