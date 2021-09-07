#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

NAME = "scrapy-redis-sentinel"
FOLDER = "scrapy_redis_sentinel"
DESCRIPTION = "Redis Cluster for Scrapy."
EMAIL = "shitao0418@gmail.com"
AUTHOR = "Shi Tao"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = None


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines() if not line.startswith("#")]


REQUIRED = read_requirements("requirements.txt")

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION
print(long_description)
about = {}
if not VERSION:
    with open(os.path.join(here, FOLDER, "__init__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        sys.exit()


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    url='https://github.com/crawlmap/scrapy-redis-sentinel.git',
    project_urls={"Documentation": "https://crawlaio.com/scrapy-redis-sentinel/"},
    packages=find_packages(),
    install_requires=REQUIRED,
    license="MIT",
    zip_safe=False,
    keywords=[
        'scrapy-redis',
        'scrapy-redis-sentinel',
        'scrapy-redis-cluster'
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    cmdclass={"upload": UploadCommand},
)
