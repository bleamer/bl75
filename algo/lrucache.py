""" LRU Cache implementation

Returns:
    LRU Cache - Least recently use cache implementation
    which takes size as the maximum capacity of cache
"""
from collections import OrderedDict

class LRUCache():
    """LRUCache Class implementing LRUCache with a given size
    """
    def __init__(self, size = 2):
        self.cache = OrderedDict()
        self.size = size

    
    def get(self, k: int):
        if k in self.cache:
            item = self.cache.get(k)
            self.cache.move_to_end(k)
        else:
            item = -1
        return item
    
    def put(self, key:int, value:any):
        self.cache[key]=value
        self.cache.move_to_end(key)
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    lrucache = LRUCache(3)
    lrucache.put(1,1)
    lrucache.put(2,22)
    print(lrucache.cache)
    print(lrucache.get(1))
    print(lrucache.cache)
    lrucache.put(3,33)
    lrucache.put(4,44)
    lrucache.put(5,55)
    print(lrucache.get(2))
    print(lrucache.get(1))
    print(lrucache.cache)