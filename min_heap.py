import time
from math import floor
from random import randint


class MinHeap:
    def __init__(self):
        self.array = []

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
        return self.array[self._lchild_index(i)]

    def _rchild(self, i):
        return self.array[self._rchild_index(i)]

    def _parent(self, i):
        return self.array[self._parent_index(i)]

    def _swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def _bubble_up(self, i):
        if i == 0:
            return
        if self.array[i] < self._parent(i):
            self._swap(i, self._parent_index(i))
            self._bubble_up(self._parent_index(i))

    def _bubble_down(self, i):
        smallest_index = i

        if self._lchild_index(i) < len(self.array) and self._lchild(i) < self.array[smallest_index]:
            smallest_index = self._lchild_index(i)

        if self._rchild_index(i) < len(self.array) and self._rchild(i) < self.array[smallest_index]:
            smallest_index = self._rchild_index(i)

        if smallest_index != i:
            self._swap(i, smallest_index)
            self._bubble_down(smallest_index)

    def heappush(self, item):
        self.array.append(item)
        if item < self._parent(len(self.array) - 1):
            self._bubble_up(len(self.array) - 1)

    def heappop(self):
        if len(self.array) == 1:
            return self.array.pop()

        min_item = self.array[0]
        self.array[0] = self.array.pop()
        self._bubble_down(0)

        return min_item

    def get_min(self):
        return self.array[0]


if __name__ == '__main__':
    start = time.time()
    h = MinHeap()
    for i in range(10):
        h.heappush(randint(-1000000, 1000000))
    print(h.array)
    while len(h.array) > 0:
        h.heappop()
    end = time.time()
    print(end - start)