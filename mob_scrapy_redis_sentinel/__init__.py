# -*- coding: utf-8 -*-

__original_author__ = "Rolando Espinoza"
__author__ = "luzihang"
__email__ = "luzihang@mob.com"
__version__ = "0.8"

from mob_tools.mobLog import MobLoguru
from mob_tools.inner_ip import get_inner_ip

inner_ip = get_inner_ip()

PRODUCTION_ENV_TAG = '10.90'
# 不是以10.90开头的，认为是非生产环境
if inner_ip.startswith(PRODUCTION_ENV_TAG):
    mob_log = MobLoguru(deep=2, log_file='/data/logs/crawler/crawler.log.es')
else:
    mob_log = MobLoguru()
    inner_ip = "127.0.0.1"
