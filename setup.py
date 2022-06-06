# !/usr/bin/env python
# _*_coding: utf-8 _*_

import codecs
import os

try:
    from setuptools import setup
except:
    from distutils.core import setup
"""
打包的用的setup必须引入，
"""


def read(fname):
    """
    定义一个read方法，用来读取目录下的长描述
    我们一般是将README文件中的内容读取出来作为长描述，这个会在PyPI中你这个包的页面上展现出来，
    你也可以不用这个方法，自己手动写内容即可，
    PyPI上支持.rst格式的文件。暂不支持.md格式的文件，<BR>.rst文件PyPI会自动把它转为HTML形式显示在你包的信息页面上。
    """
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


# 名字，一般放你包的名字即可
NAME = "mob_scrapy_redis_sentinel"

# 包含的包，可以多个，这是一个列表
PACKAGES = ["mob_scrapy_redis_sentinel"]

# 关于这个包的描述
DESCRIPTION = "this is a tool package for mobTech."

# 参见 read 方法说明
LONG_DESCRIPTION = read("README.md")

# 当前包的一些关键字，方便PyPI进行分类
KEYWORDS = "mob utils"

# 作者
AUTHOR = "LuZiHang"

# 作者邮箱
AUTHOR_EMAIL = "luzihang@mob.com"

# 你这个包的项目地址
URL = "https://github.com/pypa/sampleproject"

# 自己控制的版本号
VERSION = "0.5"

# 授权方式
LICENSE = "MIT"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
