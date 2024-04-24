import codecs
import os

from setuptools import find_packages, setup

VERSION = '0.0.1'
DESCRIPTION = 'Tattva Programming Language'

# Setting up
setup(
    name="tattva",
    version=VERSION,
    author="ABC",
    author_email="<mail@bhaskars.co@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'tattva'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)