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
SCHEDULER_QUEUE_CLASS = "mob_scrapy_redis_sentinel.queue.PriorityQueue"
SCHEDULER_DUPEFILTER_KEY = "%(spider)s:dupefilter"
SCHEDULER_DUPEFILTER_CLASS = "mob_scrapy_redis_sentinel.dupefilter.RedisDupeFilter"

SCHEDULER_PERSIST = False

START_URLS_KEY = "%(name)s:start_urls"
START_URLS_AS_SET = False
START_URLS_AS_ZSET = False

# 最近一次队列备份（任务防丢）
"""
spider opened，读取 LATEST_QUEUE_KEY。获取上一次，stop 之前，最后一次的queue data；
每次make request from data，备份一份数据，到 LATEST_QUEUE_KEY。同时删除上一批的备份。（多个worker，删除同一个 LATEST_QUEUE_KEY，如何做到不互相干扰？）
"""
LATEST_QUEUE_KEY = "%(name)s:latest_queue"
