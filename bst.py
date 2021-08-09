from typing import Optional, Iterable


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self):
        return str(self.data)

    def is_leaf(self):
        return self.left is None and self.right is None


class BST:
    def __init__(self, data: Optional[Iterable] = None):
        self.root: Optional[Node] = None
        self.size = 0
        if data is not None:
            for i in data:
                self.insert(i)

    def insert_from_iterable(self, data: Iterable):
        for i in data:
            self.insert(i)

    def empty(self):
        return self.root is None

    def insert(self, data):
        self.root = self._insert(data, self.root)
        self.size += 1

    def _insert(self, data, curr: Optional[Node]):
        if curr is None:
            return Node(data)
        elif data <= curr.data:
            curr.left = self._insert(data, curr.left)
        elif data > curr.data:
            curr.right = self._insert(data, curr.right)
        return curr

    def member(self, data):
        return self._member(data, self.root)

    def _member(self, data, curr: Optional[Node]):
        if curr is None:
            return False
        elif data == curr.data:
            return True
        elif data < curr.data:
            return self._member(data, curr.left)
        elif data > curr.data:
            return self._member(data, curr.right)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, curr: Optional[Node]):
        if curr is not None:
            self._inorder(curr.left)
            print(curr.data, end=' ')
            self._inorder(curr.right)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, curr: Optional[Node]):
        if curr is not None:
            print(curr.data, end=' ')
            self._inorder(curr.left)
            self._inorder(curr.right)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, curr: Optional[Node]):
        if curr is not None:
            self._inorder(curr.left)
            self._inorder(curr.right)
            print(curr.data, end=' ')

    def remove(self, data):
        if self.empty():
            raise ValueError('BST.remove(x): x not in BST')
        else:
            self._remove(data, self.root)

    def _remove(self, data, curr: Optional[Node]):
        if curr is None:
            raise ValueError('BST.remove(x): x not in BST')
        elif data < curr.data:
            curr.left = self._remove(data, curr.left)
        elif data > curr.data:
            curr.right = self._remove(data, curr.right)
        else:
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                pred = self.predecessor(curr.left)
                curr.data = pred.data
                curr.left = self._remove(curr.data, curr.left)
        return curr

    @staticmethod
    def predecessor(curr: Node):
        while curr.right is not None:
            curr = curr.right
        return curr


if __name__ == '__main__':
    t = BST()
    for i in [5,3,8,7,9]:
        t.insert(i)
    t.inorder()


