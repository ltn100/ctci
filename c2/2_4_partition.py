import pytest
from contextlib import ExitStack as does_not_raise
from linkedlist import Node


class Solution:
    def partition(self, node, x):
        """
        Partition a list into a left and right section, with a given boundary value x.

        Create two lists (using dummy nodes), and add each item of the list to the appropriate
        partition. Then join the lists, and return.

        :param node: Head node of list
        :param x: Partition boundary. Left partition < x. Right partition >= x
        :return:
        """
        dummy_left = left = Node()
        dummy_right = right = Node()

        curr = node
        while curr is not None:
            if curr.val < x:
                left.next = curr
                left = left.next
                right.next = curr.next
            else:
                right.next = curr
                right = right.next
                left.next = curr.next
            curr = curr.next

        left.next = dummy_right.next

        return dummy_left.next


testdata = [
    ((Node.from_array([3, 5, 8, 5, 10, 2, 1]), 5), Node.from_array([3, 2, 1, 5, 8, 5, 10]), does_not_raise()),
    ((Node.from_array([10, 11, 12, 13, 1, 2, 3]), 5), Node.from_array([1, 2, 3, 10, 11, 12, 13]), does_not_raise()),
    ((Node.from_array([1, 2, 3]), 5), Node.from_array([1, 2, 3]), does_not_raise()),
    ((Node.from_array([11, 12, 13]), 5), Node.from_array([11, 12, 13]), does_not_raise()),
    ((Node.from_array([0, -3, 1, -4, 3, -20, 5]), 0), Node.from_array([-3, -4, -20, 0, 1, 3, 5]), does_not_raise()),
    ((Node.from_array([]), 0), Node.from_array([]), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.partition(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
