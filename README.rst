scrapy-redis 集群版
===================

|PyPI| |PyPI - License| |GitHub last commit| |PyPI - Downloads|

本项目基于原项目 `scrpy-redis <https://github.com/rmax/scrapy-redis>`__ 进行修改，修改内容如下：

1. 添加了 Redis 哨兵连接支持
2. 添加了 Redis 集群连接支持
3. TODO 去重

安装
----

.. code:: bash

    pip install scrapy-redis-sentinel --user

配置示例
--------

    原版本 scrpy-redis 的所有配置都支持, 优先级：哨兵模式 > 集群模式 > 单机模式

.. code:: python

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
        "password": "password",
        "db": 0
    }

    # ----------------------------------------Scrapy 其他参数-------------------------------------

    # 在 redis 中保持 scrapy-redis 用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理 redis queues
    SCHEDULER_PERSIST = True
    # 调度队列
    SCHEDULER = "scrapy_redis_sentinel.scheduler.Scheduler"
    # 去重
    DUPEFILTER_CLASS = "scrapy_redis_sentinel.dupefilter.RFPDupeFilter"

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

问题
----

ridis 包版本不正确

.. code:: bash

      File "C:\Python37\lib\site-packages\rediscluster\nodemanager.py", line 12, in <module>
        from redis._compat import b, unicode, bytes, long, basestring
    ImportError: cannot import name 'b' from 'redis._compat' (C:\Users\Sitoi\AppData\Roaming\Python\Python37\site-packages\redis\_compat.py)

解决方案：

.. code:: bash

    pip uninstall redis -y
    pip install redis==2.10.6

.. |PyPI| image:: https://img.shields.io/pypi/v/scrapy-redis-sentinel
.. |PyPI - License| image:: https://img.shields.io/pypi/l/scrapy-redis-sentinel
.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/Sitoi/scrapy-redis-sentinel
.. |PyPI - Downloads| image:: https://img.shields.io/pypi/dw/scrapy-redis-sentinel

