#lc-146 LRU Cache Linked List

class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0) # Dummy node
        self.tail = Node(0,0) # Dummy node, will not be used in actually
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node:Node) -> int:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


    def _add_to_head(self, node:Node) -> int:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        elif len(self.cache) == self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

        new_node = Node(key, value)
        self._add_to_head(new_node)
        self.cache[key] = new_node