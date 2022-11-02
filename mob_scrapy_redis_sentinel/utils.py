# -*- coding: utf-8 -*-
import six
from hashlib import md5


def bytes_to_str(s, encoding="utf-8"):
    """Returns a str if a bytes object is given."""
    if six.PY3 and isinstance(s, bytes):
        return s.decode(encoding)
    return s


def make_md5(text):
    """
    make text to md5
    """
    return md5(str(text).encode('utf-8')).hexdigest()


def get_track_id(request):
    track_id = ''
    try:
        track_id = request.meta.get("track_id")
    except Exception:
        pass
    return track_id
