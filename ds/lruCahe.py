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
        if not node.prev:
            self.head = node.next
        else:
            node.prev.next = node.next

        if not node.next:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        # reset node neighbours pointers
        node.next = None
        node.prev = None

    def add_to_back(self, node: Node):
        if not self.head and not self.tail:
            self.head = self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def get(self, key: str) -> Optional[str]:
        if not key in self.cache:
            return None

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
            return

        # if the value exists move it from its positon to the back of the list
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_from_position(node)
            self.add_to_back(node)

        # when value doesn't exist in the list, add value to the back of list
        else:
            node = self.make_node(key, value)
            self.add_to_back(node)
            self.cache[key] = node
            self.count += 1
            self.attempt_evict_lru()

    def print_list_asc(self):
        nodes = []
        cursor = self.head
        while cursor != None:
            nodes.append({'key': cursor.key, 'value': cursor.value})
            cursor = cursor.next

        print(nodes)

    def remove(self, key: str):
        if (not self.head and not self.tail) or key not in self.cache:
            return

        node = self.cache[key]
        self.remove_from_position(node)
        self.count -= 1
        del self.cache[key]


def test_should_set_key_value_pair():
    lru = LRUCache()
    prev_count = lru.count
    key = 'foo'
    lru.set(key, 'bar')
    assert (lru.count == prev_count + 1)
    assert (key in lru.cache)


def test_should_update_same_key():
    lru = LRUCache()
    prev_count = lru.count
    key = 'foo'
    old_value = 'bar'
    new_value = 'baz'
    lru.set(key, old_value)
    lru.set(key, new_value)
    assert (lru.count == prev_count + 1)
    assert (lru.get(key) == new_value)


def test_should_get_value_for_key():
    lru = LRUCache()
    key = 'foo'
    value = 'bar'
    lru.set(key, value)
    assert (lru.get(key) == value)


def test_should_evict_lru():
    capacity = 3
    lru = LRUCache(capacity=capacity)
    lru.set('a', '1')
    lru.set('b', '2')
    lru.set('c', '3')
    lru.set('d', '4')
    lru.set('e', '5')
    assert (lru.count == capacity)
    assert (lru.get('a') == None)
    assert (lru.get('b') == None)


def test_should_remove_key_value_pair():
    lru = LRUCache()
    prev_count = lru.count
    key = 'foo'
    lru.set(key, 'bar')
    assert (lru.count == prev_count + 1)
    lru.remove(key)
    assert (lru.count == prev_count)
    assert (lru.get(key) == None)


if __name__ == '__main__':
    test_should_set_key_value_pair()
    test_should_update_same_key()
    test_should_get_value_for_key()
    test_should_evict_lru()
    test_should_remove_key_value_pair()
    print('tests passed')
