from typing import Optional, Iterable


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data: Optional[Iterable] = None):
        self.head = None
        self.tail = None
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

    def insert_back(self, data):
        new = Node(data)
        if self.empty():
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

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
        else:
            curr = self.head
            while curr.next is not None:
                if curr.next.data == data:
                    if curr.next == self.tail:
                        self.tail = curr
                        self.tail.next = None
                    else:
                        curr.next = curr.next.next
                    return
                curr = curr.next
            raise ValueError('LinkedList.remove(x): x not in LinkedList')
