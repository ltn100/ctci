import pytest
import random
from collections import Counter


class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1

    def __repr__(self):
        return str(self.val)

    def insert(self, val):
        if val <= self.val:
            if self.left is None:
                self.left = BSTNode(val)
                self.size += 1
                return self.left
            else:
                node = self.left.insert(val)
                self.size += 1
                return node
        else:
            if self.right is None:
                self.right = BSTNode(val)
                self.size += 1
                return self.right
            else:
                node = self.right.insert(val)
                self.size += 1
                return node

    def delete(self, val):
        # TODO
        pass

    def find(self, val):
        if val == self.val:
            return self
        if val <= self.val:
            if self.left is None:
                return None
            else:
                return self.left.find(val)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(val)

    def get_random(self):
        index = random.randint(1, self.size)  # inclusive
        if index == 1:
            return self
        index -= 1
        if self.left and index <= self.left.size:
            return self.left.get_random()
        return self.right.get_random()


class BSTRandom:
    """
    A binary search tree class with insert, remove, find and get_random functions.
    """
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = BSTNode(val)
            return self.root

        return self.root.insert(val)

    def find(self, val):
        if self.root is None:
            return None
        else:
            return self.root.find(val)

    def get_random(self):
        if self.root is None:
            return None
        else:
            return self.root.get_random()


def test_solution():
    bst = BSTRandom()
    bst.insert(20)
    assert bst.root.size == 1
    bst.insert(10)
    assert bst.root.size == 2
    assert bst.root.left.size == 1
    bst.insert(5)
    bst.insert(4)
    thirty = bst.insert(30)
    assert bst.root.size == 5
    assert bst.root.left.size == 3
    assert bst.root.right.size == 1
    assert bst.find(30) == thirty

    results = Counter()
    for _ in range(200):
        results[bst.get_random().val] += 1

    assert len(results) == 5
    assert results[20] > 10
    assert results[10] > 10
    assert results[5] > 10
    assert results[4] > 10
    assert results[30] > 10


if __name__ == '__main__':
    pytest.main(args=[__file__])
