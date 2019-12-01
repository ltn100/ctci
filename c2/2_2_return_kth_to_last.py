import pytest
from contextlib import ExitStack as does_not_raise
from linkedlist import Node


class Solution:
    def kth_to_last(self, node, k):
        """
        Return the kth from last node.

        Use two pointers and iterate both of them, maintaining a constant gap of k. When p1 (leading)
        hits the end, return p2.

        :param node: Head node
        :param k: int
        :return: Kth from last node
        """
        p1 = p2 = node
        for _ in range(k):
            if p1 is None:
                raise IndexError("out of bounds")
            p1 = p1.next

        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p2


testdata = [
    ((Node.from_array([1, 6, 2, 5, 5, 7, 8, 1, 9, 2, 4, 8]), 3), Node.from_array([2, 4, 8]), does_not_raise()),
    ((Node.from_array([1, 1, 1, 1, 1]), 2), Node.from_array([1, 1]), does_not_raise()),
    ((Node.from_array([1, 1]), 2), Node.from_array([1, 1]), does_not_raise()),
    ((Node.from_array([1]), 2), None, pytest.raises(IndexError)),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.kth_to_last(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
