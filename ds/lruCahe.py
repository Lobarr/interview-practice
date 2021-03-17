from typing import Optional, Dict

class Node:
    def __init__(self):
        self.key: str
        self.value: str
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity=5):
        self.capacity: int = capacity
        self.count: int = 0
        self.cache: Dict[str, Node] = {}
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def remove_from_position(self, node: Node):
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

    def add_to_back(self, node: Node):
        if not self.head and not self.tail:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def get(self, key: str) -> Optional[str]:
        if not key in self.cache:
            raise Exception('key does not exist')

        node = self.cache[key]
        self.remove_from_position(node)
        self.add_to_back(node)

        return node.value

    def attempt_evict_lru(self):
        if not self.head and not self.tail:
            return

        # when capacity threshold is hit, evict lru node 
        if self.count > self.capacity:
            prev_head = self.head
            self.head = self.head.next

            del self.cache[prev_head.key]
            self.count -= 1

    def make_node(self, key: str, value: str) -> Node:
        node = Node()
        node.key = key
        node.value = value
        return node


    def set(self, key: str, value: str):
        # set head and tail as new node when list is empty
        if not self.head and not self.tail:
            node = self.make_node(key, value)
            self.head = self.tail = node
            self.cache[key] = node
            self.count += 1
            self.attempt_evict_lru()
            return

        # if the value exists move it from its positon to the back of the list
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_from_position(node)
            self.add_to_back(node)

        # when value doesn't exist in the list, set value to second to last
        # recently used
        else:
            node = self.make_node(key, value)
            prev_next = self.head.next
            node.next = prev_next
            node.prev = self.head

            if prev_next:
                prev_next.prev = node

            self.head.next = node
            self.cache[key] = node
            self.count += 1
            self.attempt_evict_lru()

    def remove(self, key: str):
        pass


if __name__ == '__main__':
    lru = LRUCache(capacity=3)
    lru.set('foo', 'bar')
    print(lru.count)
    lru.set('jane', 'doe')
    print(lru.count)
    print(lru.get('foo'))
    print(lru.get('jane'))
    lru.set('foo', 'baz')
    print(lru.get('foo'))
    print(lru.count)
    lru.set('fooz', 'bark')
    print(lru.count)
    print(lru.get('fooz'))
    lru.set('janet', 'doez')
    print(lru.count)
    print(lru.get('janet'))


