#!/usr/bin/python3
"""BaseCaching module"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache Algorithms
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adding elements to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key not in self.queue:
            self.queue.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_in = self.queue.pop(0)
            if first_in in self.cache_data:
                del self.cache_data[first_in]
                print("DISCARD: {}".format(first_in))

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
