import redis

# For standalone use.
import rediscluster
from redis.sentinel import Sentinel

DUPEFILTER_KEY = "dupefilter:%(timestamp)s"

PIPELINE_KEY = "%(spider)s:items"

REDIS_CLS = redis.StrictRedis
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
SCHEDULER_DUPEFILTER_CLASS = "scrapy_redis_sentinel.dupefilter.RFPDupeFilter"

START_URLS_KEY = "%(name)s:start_urls"
START_URLS_AS_SET = False

REDIS_CLUSTER_CLS = rediscluster.RedisCluster
REDIS_SENTINEL_CLS = Sentinel
