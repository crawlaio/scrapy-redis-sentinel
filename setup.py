#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='scrapy-redis-sentinel',
    description="Redis Cluster for Scrapy.",
    author="Shi Tao",
    author_email='shitao0418@gmail.com',
    url='https://github.com/Sitoi/scrapy-redis-cluster.git',
    packages=find_packages(),
    install_requires=[
        'Scrapy>=1.0',
        'redis>=2.10',
        'six>=1.5.2',
        'redis-py-cluster>=1.3.4',
    ],
    license="MIT",
    keywords=[
        'scrapy-redis-sentinel',
        'scrapy-redis-cluster'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
