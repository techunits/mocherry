#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mocherry",
    version="1.0.3",
    author="Sougata P.",
    author_email="skall.paul@gmail.com",
    description="CherryPy REST webservice framework with MongoDB ORM support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/techunits/mocherry",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'wheel',
        'cherrypy',
        'cherrypy_cors',
        'routes',
        'mongoengine',
        'requests',
    ],
    # extras_require={
    #     'win32': 'pypiwin32'
    # },
    python_requires='>=3.6',
)
