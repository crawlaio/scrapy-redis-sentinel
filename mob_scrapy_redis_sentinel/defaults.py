# -*- coding: utf-8 -*-
import redis
import os
import rediscluster
from redis.sentinel import Sentinel

from mob_scrapy_redis_sentinel import inner_ip, mob_log

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

"""
从MQ获取任务
"""
MQ_USED = False  # 默认关闭

MQ_HOST = "http://10.89.104.148:10011"
# 从指定队列中取出消息
POP_MESSAGE = MQ_HOST + "/rest/ms/GemMQ/popMessage?queueName={queueName}"
# 获取消息队列的大小
GET_QUEUE_SIZE = MQ_HOST + "/rest/ms/GemMQ/getQueueSize?queueName={queueName}"

# 与环境相关的配置
PRODUCTION_ENV_TAG = '10.90'
local_ip = os.getenv("LOCAL_IP", inner_ip)
# 不是以10.90开头的，认为是非生产环境
if local_ip.startswith(PRODUCTION_ENV_TAG):
    QUEUE_NAME_PREFIX = "CRAWLER-UQ-{}"
else:
    QUEUE_NAME_PREFIX = "CRAWLER-SANDBOX-UQ-{}"
