from typing import Optional, Any, Union

Hashable = Union[int, float, bool, str, bytes]


class Node:
    def __init__(self, key: Hashable, value: Any):
        self.key: Hashable = key
        self.value: Any = value
        self.next: Optional[Node] = None

    def __repr__(self):
        rep = f"Node({self.key}: {self.value})"
        curr_node = self
        while curr_node.next is not None:
            curr_node = curr_node.next
            rep += f" -> Node({curr_node.key}: {curr_node.value})"
        return rep


class HashTable:
    INITIAL_SIZE = 7919

    def __init__(self, **kwargs):
        self.buckets: list[Optional[Node]] = [None for _ in range(self.INITIAL_SIZE)]
        for k, v in kwargs.items():
            self.insert(k, v)

    def __repr__(self):
        return f"HashTable({', '.join([str(n) for n in self.buckets if n is not None])})"

    def hash_fn(self, key: Hashable) -> int:
        i = 7
        for c in str(key):
            i += ord(c)
            i *= 7

        return i % self.INITIAL_SIZE

    def insert(self, key: Hashable, value: Any):
        i = self.hash_fn(key)
        curr_node = self.buckets[i]

        while curr_node is not None:
            if curr_node.key == key:
                curr_node.value = value
                return
            if curr_node.next is None:
                curr_node.next = Node(key, value)
                return
            curr_node = curr_node.next

        self.buckets[i] = Node(key, value)

    def get(self, key: Hashable) -> Optional[Any]:
        curr_node = self.buckets[self.hash_fn(key)]

        while curr_node is not None and curr_node.key != key:
            curr_node = curr_node.next

        if curr_node is None:
            raise KeyError(f"key '{key}' not in Hash Table")
        else:
            return curr_node.value

    def remove(self, key: Hashable):
        i = self.hash_fn(key)
        curr_node = self.buckets[i]

        prev = None
        while curr_node is not None and curr_node.key != key:
            prev = curr_node
            curr_node = prev.next

        if curr_node is None:
            raise KeyError(f"key '{key}' not in Hash Table")
        if prev is None:
            self.buckets[i] = curr_node.next
        else:
            prev.next = curr_node.next



if __name__ == '__main__':
    d = HashTable(a=1, b=2, c=3)
    d.insert("d", 4)
    print(d)
    d.remove("b")
    print(d)
