#!/usr/bin/env python3
""" LRUCaching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache Class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """Assign item value for the key"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_keys.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.cache_keys.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.cache_keys.append(key)

    def get(self, key):
        """Return the value linked to key"""
        if key is None or key not in self.cache_data:
            return None

        self.cache_keys.remove(key)
        self.cache_keys.append(key)
        return self.cache_data[key]
