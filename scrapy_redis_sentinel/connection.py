# -*- coding: utf-8 -*-
import sys

import six
from scrapy.utils.misc import load_object

from . import defaults

# Shortcut maps 'setting name' -> 'parmater name'.
SETTINGS_PARAMS_MAP = {
    "REDIS_URL": "url",
    "REDIS_HOST": "host",
    "REDIS_PORT": "port",
    "REDIS_DB": "db",
    "REDIS_ENCODING": "encoding"
}

if sys.version_info > (3,):
    SETTINGS_PARAMS_MAP["REDIS_DECODE_RESPONSES"] = "decode_responses"


def get_redis_from_settings(settings):
    """Returns a redis client instance from given Scrapy settings object.

    This function uses ``get_client`` to instantiate the client and uses
    ``defaults.REDIS_PARAMS`` global as defaults values for the parameters. You
    can override them using the ``REDIS_PARAMS`` setting.

    Parameters
    ----------
    settings : Settings
        A scrapy settings object. See the supported settings below.

    Returns
    -------
    server
        Redis client instance.

    Other Parameters
    ----------------
    REDIS_URL : str, optional
        Server connection URL.
    REDIS_HOST : str, optional
        Server host.
    REDIS_PORT : str, optional
        Server port.
    REDIS_ENCODING : str, optional
        Data encoding.
    REDIS_PARAMS : dict, optional
        Additional client parameters.

    """
    params = defaults.REDIS_PARAMS.copy()
    params.update(settings.getdict("REDIS_PARAMS"))
    # XXX: Deprecate REDIS_* settings.
    for source, dest in SETTINGS_PARAMS_MAP.items():
        val = settings.get(source)
        if val:
            params[dest] = val

    # Allow ``redis_cls`` to be a path to a class.
    if isinstance(params.get("redis_cls"), six.string_types):
        params["redis_cls"] = load_object(params["redis_cls"])

    return get_redis(**params)


# Backwards compatible alias.
# from_settings = get_redis_from_settings


def get_redis(**kwargs):
    """Returns a redis client instance.

    Parameters
    ----------
    redis_cls : class, optional
        Defaults to ``redis.StrictRedis``.
    url : str, optional
        If given, ``redis_cls.from_url`` is used to instantiate the class.
    **kwargs
        Extra parameters to be passed to the ``redis_cls`` class.

    Returns
    -------
    server
        Redis client instance.

    """
    redis_cls = kwargs.pop("redis_cls", defaults.REDIS_CLS)
    url = kwargs.pop("url", None)
    if url:
        return redis_cls.from_url(url, **kwargs)
    else:
        return redis_cls(**kwargs)


# 集群连接配置
REDIS_CLUSTER_SETTINGS_PARAMS_MAP = {
    "REDIS_CLUSTER_URL": "url",
    "REDIS_CLUSTER_HOST": "host",
    "REDIS_CLUSTER_PORT": "port",
    "REDIS_CLUSTER_ENCODING": "encoding"
}


def get_redis_cluster_from_settings(settings):
    """
    Returns a redis cluster instance from given Scrapy settings object.

    :param settings:
    :return:
    """
    params = defaults.REDIS_PARAMS.copy()
    params.update(settings.getdict("REDIS_CLUSTER_PARAMS"))
    params.setdefault("startup_nodes", settings.get("REDIS_STARTUP_NODES"))
    # XXX: Deprecate REDIS_* settings.
    for source, dest in REDIS_CLUSTER_SETTINGS_PARAMS_MAP.items():
        val = settings.get(source)
        if val:
            params[dest] = val

    return get_redis_cluster(**params)


def get_redis_cluster(**kwargs):
    """
    Returns a redis cluster instance.

    :param kwargs:
    :return:
    """
    redis_cluster_cls = kwargs.get("redis_cluster_cls", defaults.REDIS_CLUSTER_CLS)
    url = kwargs.pop("url", None)
    redis_nodes = kwargs.pop("startup_nodes", None)
    if redis_nodes:
        return redis_cluster_cls(startup_nodes=redis_nodes, **kwargs)
    if url:
        return redis_cluster_cls.from_url(url, **kwargs)
    return redis_cluster_cls(**kwargs)


# 哨兵连接配置
def get_redis_sentinel_from_settings(settings):
    """
    Returns a redis sentinel instance from given Scrapy settings object.

    :param settings:
    :return:
    """
    params = defaults.REDIS_PARAMS.copy()
    params.update(settings.getdict("REDIS_SENTINEL_PARAMS"))
    params.setdefault("sentinels", settings.get("REDIS_SENTINELS"))
    params.setdefault("socket_timeout", settings.get("REDIS_SENTINELS_SOCKET_TIMEOUT"))
    return get_redis_sentinel(**params)


def get_redis_sentinel(**kwargs):
    """
    Returns a sentinel cluster instance.

    :param kwargs:
    :return:
    """
    redis_sentinel_cls = kwargs.get("redis_cluster_cls", defaults.REDIS_SENTINEL_CLS)
    sentinels = kwargs.pop("sentinels", None)
    socket_timeout = kwargs.pop("socket_timeout", 0.5)
    redis_sentinel_cls = redis_sentinel_cls(sentinels=sentinels, socket_timeout=socket_timeout)
    redis_cls = redis_sentinel_cls.master_for(**kwargs)
    return redis_cls


def from_settings(settings):
    """
    Select the connection method of redis according to the configuration in settings

    :param settings:
    :return:
    """
    if "REDIS_SENTINELS" in settings:
        return get_redis_sentinel_from_settings(settings)
    elif "REDIS_STARTUP_NODES" in settings or "REDIS_CLUSTER_URL" in settings:
        return get_redis_cluster_from_settings(settings)
    return get_redis_from_settings(settings)
