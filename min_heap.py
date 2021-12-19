from math import floor
import random


class MinHeap:
    def __init__(self):
        self._array = []

    def __repr__(self):
        return f"MinHeap({self._array})"

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
        if self._array[i] < self._parent(i):
            self._swap(i, self._parent_index(i))
            self._bubble_up(self._parent_index(i))

    def _bubble_down(self, i):
        smallest_index = i

        if self._lchild_index(i) < len(self._array) and self._lchild(i) < self._array[smallest_index]:
            smallest_index = self._lchild_index(i)

        if self._rchild_index(i) < len(self._array) and self._rchild(i) < self._array[smallest_index]:
            smallest_index = self._rchild_index(i)

        if smallest_index != i:
            self._swap(i, smallest_index)
            self._bubble_down(smallest_index)

    def heappush(self, item):
        self._array.append(item)
        if item < self._parent(len(self._array) - 1):
            self._bubble_up(len(self._array) - 1)

    def heappop(self):
        if len(self._array) == 1:
            return self._array.pop()

        min_item = self._array[0]
        self._array[0] = self._array.pop()
        self._bubble_down(0)

        return min_item

    def heappushpop(self, item):
        if item < self._array[0]:
            return item

        min_item = self._array[0]
        self._array[0] = item
        self._bubble_down(0)
        return min_item

    def heapreplace(self, item):
        min_item = self._array[0]
        self._array[0] = item
        self._bubble_down(0)
        return min_item

    def get_min(self):
        return self._array[0]

    @staticmethod
    def heapsort(l):
        h = MinHeap()
        for i in l:
            h.heappush(i)

        sorted_l = []
        while h:
            sorted_l.append(h.heappop())

        return sorted_l

    @classmethod
    def heapify(cls, l):
        h = MinHeap()
        h._array = l[:]
        for i in range(len(h) // 2, -1, -1):
            h._bubble_down(i)

        return h
