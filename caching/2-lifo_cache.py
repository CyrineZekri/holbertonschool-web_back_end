#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache class:
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.order.pop(-2)  
                del self.cache_data[last_key]
                print("DISCARD:", last_key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
