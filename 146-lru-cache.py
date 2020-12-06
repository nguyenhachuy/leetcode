class Node:
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.sentinel = Node(-1,-1)
        self.end = Node(-1,-1)
        self.sentinel.next = self.end
        self.end.prev = self.sentinel
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        node = self.table[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.sentinel.next
        node.prev = self.sentinel
        self.sentinel.next.prev = node
        self.sentinel.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            node.val = value
            self.get(key)
        else:
            node = Node(key, value)
            self.table[key] = node
            node.next = self.sentinel.next
            node.prev = self.sentinel
            self.sentinel.next.prev = node
            self.sentinel.next = node
            self.size += 1

        if self.size > self.capacity:
            self.size -= 1
            node_to_delete = self.end.prev
            del self.table[node_to_delete.key]
            self.end.prev = node_to_delete.prev
            node_to_delete.prev.next = self.end





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
left side has min, right side has min,
then combine might stilll be better
"""
