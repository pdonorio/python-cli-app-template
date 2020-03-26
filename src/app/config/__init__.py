"""
inspired from
http://pythonwise.blogspot.com/2020/03/using-getattr-for-nicer-configuration.html
"""
import json


def class2dict_repr(obj):
    if hasattr(obj, '__dict__'):
        values = obj.__dict__  # .get(key, {})
    else:
        values = obj
    return json.dumps(values, indent=2)


class ConfigWrapper:
    def __init__(self, cfg):
        self._cfg = cfg

    def __getattr__(self, attr):
        try:
            val = self._cfg[attr]
            if isinstance(val, dict):
                val = ConfigWrapper(val)
            return val
        except KeyError:
            raise AttributeError(attr)

    def __dir__(self):
        return list(self._cfg)

    def __repr__(self):
        return class2dict_repr(self._cfg)

    def __str__(self):
        return class2dict_repr(self._cfg)
