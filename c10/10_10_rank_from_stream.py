import pytest
from contextlib import ExitStack as does_not_raise
from collections import Counter


class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    def insert(self, val):
        if self.val == val:
            return
        if self.val < val:
            if self.right is not None:
                return self.right.insert(val)
            self.right = BSTNode(val)
        else:
            if self.left is not None:
                return self.left.insert(val)
            self.left = BSTNode(val)

    def get_less_than_or_equal(self, val):
        result = []
        if self.val <= val:
            result.append(self.val)
            if self.left:
                result.extend(self.left.get_less_than_or_equal(val))
            if self.right:
                result.extend(self.right.get_less_than_or_equal(val))
        else:
            if self.left:
                result.extend(self.left.get_less_than_or_equal(val))
        return result


class StreamRanker:
    def __init__(self):
        self.bst_root = BSTNode(0)
        self.counter = Counter({0: 0})

    def track(self, n):
        if n not in self.counter:
            self.bst_root.insert(n)

        self.counter[n] += 1

    def get_rank(self, n):
        rank = 0
        for val in self.bst_root.get_less_than_or_equal(n):
            rank += self.counter[val]
        return rank - 1  # not including current instance


testdata = [
    (([5, 1, 4, 4, 5, 9, 7, 13, 3], 1), 0, does_not_raise()),
    (([5, 1, 4, 4, 5, 9, 7, 13, 3], 3), 1, does_not_raise()),
    (([5, 1, 4, 4, 5, 9, 7, 13, 3], 4), 3, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        stream, val = args
        sr = StreamRanker()
        for n in stream:
            sr.track(n)

        assert sr.get_rank(val) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
