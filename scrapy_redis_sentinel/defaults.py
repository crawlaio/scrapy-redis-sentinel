# -*- coding: utf-8 -*-
import redis

import rediscluster
from redis.sentinel import Sentinel

DUPEFILTER_KEY = "dupefilter:%(timestamp)s"

PIPELINE_KEY = "%(spider)s:items"

STATS_KEY = '%(spider)s:stats'

REDIS_CLS = redis.StrictRedis
REDIS_CLUSTER_CLS = rediscluster.RedisCluster
REDIS_SENTINEL_CLS = Sentinel

REDIS_ENCODING = "utf-8"
# Sane connection defaults.
REDIS_PARAMS = {
    "socket_timeout": 30,
    "socket_connect_timeout": 30,
    "retry_on_timeout": True,
    "encoding": REDIS_ENCODING
}

SCHEDULER_QUEUE_KEY = "%(spider)s:requests"
SCHEDULER_QUEUE_CLASS = "scrapy_redis_sentinel.queue.PriorityQueue"
SCHEDULER_DUPEFILTER_KEY = "%(spider)s:dupefilter"
SCHEDULER_DUPEFILTER_CLASS = "scrapy_redis_sentinel.dupefilter.RedisDupeFilter"

SCHEDULER_PERSIST = False

START_URLS_KEY = "%(name)s:start_urls"
START_URLS_AS_SET = False
START_URLS_AS_ZSET = False
