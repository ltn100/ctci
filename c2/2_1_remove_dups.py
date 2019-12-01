import pytest
from contextlib import ExitStack as does_not_raise
from linkedlist import Node


class Solution:
    def remove_dups(self, node):
        """
        Remove duplicates from an unsorted linked list.

        Iterate through LL and populate set() of unique values. If value already exists in the
        set then remove the node.

        :param node: Head node
        :return: Head node
        """
        seen = set()
        curr = node
        prev = None
        while curr is not None:
            if curr.val in seen:
                # Remove node
                prev.next = curr.next
            else:
                seen.add(curr.val)
                prev = curr
            curr = curr.next
        return node


class Solution2:
    def remove_dups(self, node):
        """
        Remove duplicates from an unsorted linked list. No temporary buffer.

        Use two pointers to iterate. Second pointer iterates across remaining list
        for each increment of first pointer. O(n^2) time, O(1) space.

        :param node: Head node
        :return: Head node
        """
        p1 = node
        while p1 is not None:
            val = p1.val
            p2 = p1.next
            prev = p1
            while p2 is not None:
                if p2.val == val:
                    # Remove node
                    prev.next = p2.next
                else:
                    prev = p2
                p2 = p2.next
            p1 = p1.next
        return node


testdata = [
    ((Node.from_array([1, 1, 1, 2, 2, 2]),), Node.from_array([1, 2]), does_not_raise()),
    ((Node.from_array([1, 2, 3]),), Node.from_array([1, 2, 3]), does_not_raise()),
    ((Node.from_array([1]),), Node.from_array([1]), does_not_raise()),
    ((Node.from_array([]),), Node.from_array([]), does_not_raise()),
    ((Node.from_array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),), Node.from_array([1]), does_not_raise()),
    ((Node.from_array([1, 6, 2, 5, 4, 8, 6, 2, 5, 7, 8, 1, 9, 2, 4, 8]),), Node.from_array([1, 6, 2, 5, 4, 8, 7, 9]), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.remove_dups(*args) == res


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution2(args, res, expectation):
    with expectation:
        s = Solution2()
        assert s.remove_dups(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
