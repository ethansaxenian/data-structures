import operator
import random
from math import floor
from typing import Union


class Heap:
    OP_MAP = {
        "<": operator.lt,
        ">": operator.gt
    }

    def __init__(self, op: Union[str, callable] = operator.lt):
        self._array = []
        if op not in ("<", ">", operator.lt, operator.gt):
            raise ValueError("op must be one of '<', '>', 'operator.lt', 'operator.gt'")
        self._op = self.OP_MAP.get(op, op)

    def __repr__(self):
        if self._op == operator.lt:
            return f"MinHeap({self._array})"
        if self._op == operator.gt:
            return f"MaxHeap({self._array})"

    def __bool__(self):
        return bool(self._array)

    def __len__(self):
        return len(self._array)

    def __getitem__(self, i):
        return self._array[i]

    @staticmethod
    def _lchild_index(i):
        return 2 * i + 1

    @staticmethod
    def _rchild_index(i):
        return 2 * i + 2

    @staticmethod
    def _parent_index(i):
        return floor((i - 1) / 2)

    def _lchild(self, i):
        return self._array[self._lchild_index(i)]

    def _rchild(self, i):
        return self._array[self._rchild_index(i)]

    def _parent(self, i):
        return self._array[self._parent_index(i)]

    def _swap(self, i, j):
        self._array[i], self._array[j] = self._array[j], self._array[i]

    def _bubble_up(self, i):
        if i == 0:
            return
        if self._op(self._array[i], self._parent(i)):
            self._swap(i, self._parent_index(i))
            self._bubble_up(self._parent_index(i))

    def _bubble_down(self, i):
        swap_index = i

        if self._lchild_index(i) < len(self._array) and self._op(self._lchild(i), self._array[swap_index]):
            swap_index = self._lchild_index(i)

        if self._rchild_index(i) < len(self._array) and self._op(self._rchild(i), self._array[swap_index]):
            swap_index = self._rchild_index(i)

        if swap_index != i:
            self._swap(i, swap_index)
            self._bubble_down(swap_index)

    def heappush(self, item):
        self._array.append(item)
        if self._op(item, self._parent(len(self._array) - 1)):
            self._bubble_up(len(self._array) - 1)

    def heappop(self):
        if len(self._array) == 1:
            return self._array.pop()

        min_item = self._array[0]
        self._array[0] = self._array.pop()
        self._bubble_down(0)

        return min_item

    def heappushpop(self, item):
        if self._op(item, self._array[0]):
            return item

        target_item = self._array[0]
        self._array[0] = item
        self._bubble_down(0)
        return target_item

    def heapreplace(self, item):
        target_item = self._array[0]
        self._array[0] = item
        self._bubble_down(0)
        return target_item

    @staticmethod
    def heapsort(l, op: Union[str, callable]):
        h = Heap(op=op)
        for i in l:
            h.heappush(i)

        sorted_l = []
        while h:
            sorted_l.append(h.heappop())

        return sorted_l

    @classmethod
    def heapify(cls, l, op: Union[str, callable]):
        h = Heap(op=op)
        h._array = l[:]
        for i in range(len(h) // 2, -1, -1):
            h._bubble_down(i)

        return h
