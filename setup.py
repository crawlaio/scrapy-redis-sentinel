# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='scrapy-redis-sentinel',
    description="Redis Cluster for Scrapy.",
    long_description=open('README.rst', encoding="utf-8").read(),
    version="0.1.6",
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
        'scrapy-redis',
        'scrapy-redis-sentinel',
        'scrapy-redis-cluster'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
