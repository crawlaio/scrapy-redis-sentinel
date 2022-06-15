# -*- coding: utf-8 -*-

__original_author__ = "Rolando Espinoza"
__author__ = "luzihang"
__email__ = "luzihang@mob.com"
__version__ = "0.5"

from mob_tools.mobLog import MobLoguru
from mob_tools.inner_ip import get_inner_ip
import os

# 环境常量
DEV = "dev"
PROD = "prod"

ENV = os.getenv("ENV", DEV)

inner_ip = os.getenv("LOCAL_IP", get_inner_ip())

PRODUCTION_ENV_TAG = '10.90'
local_ip = os.getenv("LOCAL_IP", inner_ip)
# 不是以10.90开头的，认为是非生产环境
if local_ip.startswith(PRODUCTION_ENV_TAG):
    mob_log = MobLoguru(deep=2, log_file='/data/logs/crawler/crawler.log.es')
else:
    mob_log = MobLoguru()
    inner_ip = "127.0.0.1"
