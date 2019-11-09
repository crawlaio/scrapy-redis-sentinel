scrapy-redis 集群版
===================

|PyPI| |PyPI - License| |GitHub last commit| |PyPI - Downloads|

本项目基于原项目 `scrpy-redis <https://github.com/rmax/scrapy-redis>`__

进行修改，修改内容如下：

1. 添加了 Redis 哨兵连接支持
2. 添加了 Redis 集群连接支持
3. 添加了 Bloomfilter 去重

安装
----

.. code:: bash

    pip install scrapy-redis-sentinel --user

配置示例
--------

    原版本 scrpy-redis 的所有配置都支持, 优先级：哨兵模式 > 集群模式 >
    单机模式

.. code:: python

    # ----------------------------------------Bloomfilter 配置-------------------------------------
    # 使用的哈希函数数，默认为 6
    BLOOMFILTER_HASH_NUMBER = 6

    # Bloomfilter 使用的 Redis 内存位，30 表示 2 ^ 30 = 128MB，默认为 30   (2 ^ 22 = 1MB 可去重 130W URL)
    BLOOMFILTER_BIT = 30

    # 是否开启去重调试模式 默认为 False 关闭
    DUPEFILTER_DEBUG = False

    # ----------------------------------------Redis 单机模式-------------------------------------
    # Redis 单机地址
    REDIS_HOST = "172.25.2.25"
    REDIS_PORT = 6379

    # REDIS 单机模式配置参数
    REDIS_PARAMS = {
        "password": "password",
        "db": 0
    }

    # ----------------------------------------Redis 哨兵模式-------------------------------------

    # Redis 哨兵地址
    REDIS_SENTINELS = [
        ('172.25.2.25', 26379),
        ('172.25.2.26', 26379),
        ('172.25.2.27', 26379)
    ]

    # REDIS_SENTINEL_PARAMS 哨兵模式配置参数。
    REDIS_SENTINEL_PARAMS= {
        "service_name":"mymaster",
        "password": "password",
        "db": 0
    }

    # ----------------------------------------Redis 集群模式-------------------------------------

    # Redis 集群地址
    REDIS_MASTER_NODES = [
        {"host": "172.25.2.25", "port": "6379"},
        {"host": "172.25.2.26", "port": "6379"},
        {"host": "172.25.2.27", "port": "6379"},
    ]

    # REDIS_CLUSTER_PARAMS 集群模式配置参数
    REDIS_CLUSTER_PARAMS= {
        "password": "password"
    }

    # ----------------------------------------Scrapy 其他参数-------------------------------------

    # 在 redis 中保持 scrapy-redis 用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理 redis queues
    SCHEDULER_PERSIST = True
    # 调度队列
    SCHEDULER = "scrapy_redis_sentinel.scheduler.Scheduler"
    # 去重
    DUPEFILTER_CLASS = "scrapy_redis_sentinel.dupefilter.RFPDupeFilter"

    # 指定排序爬取地址时使用的队列
    # 默认的 按优先级排序( Scrapy 默认)，由 sorted set 实现的一种非 FIFO、LIFO 方式。
    # SCHEDULER_QUEUE_CLASS = 'scrapy_redis_sentinel.queue.SpiderPriorityQueue'
    # 可选的 按先进先出排序（FIFO）
    # SCHEDULER_QUEUE_CLASS = 'scrapy_redis_sentinel.queue.SpiderStack'
    # 可选的 按后进先出排序（LIFO）
    # SCHEDULER_QUEUE_CLASS = 'scrapy_redis_sentinel.queue.SpiderStack'

    注：当使用集群时单机不生效

spiders 使用
------------

**修改 RedisSpider 引入方式**

原版本 ``scrpy-redis`` 使用方式

.. code:: python

    from scrapy_redis.spiders import RedisSpider

    class Spider(RedisSpider):
        ...

``scrapy-redis-sentinel`` 使用方式

.. code:: python

    from scrapy_redis_sentinel.spiders import RedisSpider

    class Spider(RedisSpider):
        ...

.. |PyPI| image:: https://img.shields.io/pypi/v/scrapy-redis-sentinel
.. |PyPI - License| image:: https://img.shields.io/pypi/l/scrapy-redis-sentinel
.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/Sitoi/scrapy-redis-sentinel
.. |PyPI - Downloads| image:: https://img.shields.io/pypi/dw/scrapy-redis-sentinel
