class LRUCache:
    class LRUNode:
        # double linked list and hashtable
        def __init__(self, key, value):
            self.prev = None
            self.next = None
            self.key = key
            self.value = value

    def __init__(self, capacity: int):
        self.map = { }
        self.list_head = LRUCache.LRUNode(-1, -1)
        self.list_tail = LRUCache.LRUNode(-1, -1)
        self.list_head.next = self.list_tail
        self.list_tail.prev = self.list_head
        self.capacity = capacity
        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def append_node(self, new_node):
        last_node = self.list_tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.list_tail
        self.list_tail.prev = new_node
        
    def get(self, key: int) -> int:
        if key in self.map:
            cur = self.map.get(key)
            self.remove_node(cur)
            self.append_node(cur)
            return cur.value
        else:
            return -1   

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        elif key in self.map:
            old_node = self.map.get(key)
            self.remove_node(old_node)
            old_node.value = value
            self.append_node(old_node)
        else:
            if len(self.map) >= self.capacity:
                del_node = self.list_head.next
                self.remove_node(del_node)
                del self.map[del_node.key]
            new_node = LRUCache.LRUNode(key, value)
            self.append_node(new_node)
            self.map[key] = new_node        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)