# -*- coding: utf-8 -*-

__original_author__ = "Rolando Espinoza"
__author__ = "Shi Tao"
__email__ = "shitao0418@gmail.com"
__version__ = "0.7.2"

from mob_tools.mobLog import MobLoguru
import os

# 环境常量
DEV = "dev"
PROD = "prod"

ENV = os.getenv("ENV", DEV)

if ENV == "prod":
    mob_log = MobLoguru(deep=2, log_file='/data/logs/crawler/crawler.log.es')
else:
    mob_log = MobLoguru()
