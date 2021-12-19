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

    def __init__(self, iterable: dict, **kwargs):
        self._buckets: list[Optional[Node]] = [None for _ in range(self.INITIAL_SIZE)]
        for k, v in iterable.items():
            self.insert(k, v)
        for k, v in kwargs.items():
            self.insert(k, v)

    def __repr__(self):
        return f"HashTable({', '.join([str(n) for n in self._buckets if n is not None])})"

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __delitem__(self, key):
        self.remove(key)

    def __contains__(self, key):
        return self._buckets[self._hash_fn(key)] is not None

    def _hash_fn(self, key: Hashable) -> int:
        i = 7
        for c in str(key):
            i += ord(c)
            i *= 7

        return i % self.INITIAL_SIZE

    def insert(self, key: Hashable, value: Any):
        i = self._hash_fn(key)
        curr_node = self._buckets[i]

        while curr_node is not None:
            if curr_node.key == key:
                curr_node.value = value
                return
            if curr_node.next is None:
                curr_node.next = Node(key, value)
                return
            curr_node = curr_node.next

        self._buckets[i] = Node(key, value)

    def get(self, key: Hashable) -> Optional[Any]:
        curr_node = self._buckets[self._hash_fn(key)]

        while curr_node is not None and curr_node.key != key:
            curr_node = curr_node.next

        if curr_node is None:
            raise KeyError(f"key '{key}' not in Hash Table")
        else:
            return curr_node.value

    def remove(self, key: Hashable):
        i = self._hash_fn(key)
        curr_node = self._buckets[i]

        prev = None
        while curr_node is not None and curr_node.key != key:
            prev = curr_node
            curr_node = prev.next

        if curr_node is None:
            raise KeyError(f"key '{key}' not in Hash Table")
        if prev is None:
            self._buckets[i] = curr_node.next
        else:
            prev.next = curr_node.next
