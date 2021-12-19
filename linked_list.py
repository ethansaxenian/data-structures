from typing import Optional, Iterable


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data: Optional[Iterable] = None):
        self.head = None
        self.tail = None
        self._size = 0
        if data is not None:
            for item in data:
                self.insert_back(item)

    def __repr__(self):
        return 'LinkedList(' + ', '.join(map(str, list(self))) + ')'

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    def __len__(self):
        return self._size

    def __bool__(self):
        return bool(self._size)

    def __getitem__(self, i):
        if i >= len(self):
            raise IndexError

        curr_node = self.head
        for _ in range(i):
            curr_node = curr_node.next
        return curr_node.data

    def empty(self):
        return self.head is None

    def insert_front(self, data):
        new = Node(data)
        if self.empty():
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new

        self._size += 1

    def insert_back(self, data):
        new = Node(data)
        if self.empty():
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

        self._size += 1

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def member(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
        else:
            curr = self.head
            while curr.next is not None:
                if curr.next.data == data:
                    if curr.next == self.tail:
                        self.tail = curr
                        self.tail.next = None
                    else:
                        curr.next = curr.next.next
                    self._size -= 1
                    return
                curr = curr.next
            raise ValueError('LinkedList.remove(x): x not in LinkedList')
