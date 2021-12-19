import random
from typing import Optional, Iterable, Callable, Any


class Bag:
    def __init__(self, data: Optional[Iterable] = None):
        self._data = data or []

    def __repr__(self):
        return 'Bag(' + ', '.join(map(str, self._data)) + ')'

    def __len__(self):
        return len(self._data)

    def __bool__(self):
        return bool(self._data)

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

    def __add__(self, other):
        return Bag(self._data + list(other))

    __radd__ = __add__

    def __iadd__(self, other):
        self._data += other
        return self

    def __mul__(self, other):
        return Bag(self._data * other)

    __rmul__ = __mul__

    def __imul__(self, other):
        self._data *= other
        return self

    def empty(self):
        return not bool(self)

    def add(self, item):
        self._data.append(item)

    def size(self) -> int:
        return len(self)

    def count(self, item) -> int:
        return len([i for i in self._data if i == item])

    def pop(self):
        """removes and returns a random element from the bag"""
        if not self.empty():
            return self._data.pop(random.randint(0, len(self) - 1))
        else:
            raise KeyError('pop from empty bag')

    def conform(self, predicate: Callable[[Any], bool]) -> bool:
        return all(predicate(i) for i in self._data)
