class DLL:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.hash_map = {}
        self.cur_len = 0
        self.max_len = capacity

    def move_to_front(self, node):
        if node == self.head or self.head == self.tail:
            return
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev
        if self.tail == node:
            self.tail = node.prev

        self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node

    def discard(self):
        # Discard the least recently used item, i.e. last item fromm DLL
        if self.tail is None:
            return
        node = self.tail
        # Only one element
        if self.head == node:
            self.head = node.next

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.tail = node.prev
        _ = self.hash_map.pop(node.key)

    def get_node(self, key: int) -> int:
        val = self.hash_map.get(key)
        if val:
            self.move_to_front(val)
        return val

    def get(self, key: int) -> int:
        val = self.get_node(key)
        if val:
            return val.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)

        if node:
            node.val = value
        else:
            if self.max_len == self.cur_len:
                self.discard()
                self.cur_len -= 1

            node = DLL(key, value)
            if self.head:
                node.next = self.head
                self.head.prev = node
            if self.tail is None:
                self.tail = node
            self.hash_map[key] = node
            self.cur_len += 1
        # We update head anyways
        self.head = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
