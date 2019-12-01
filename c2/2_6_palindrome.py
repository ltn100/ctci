import pytest
from contextlib import ExitStack as does_not_raise
from linkedlist import Node


class Solution:
    def is_palindrome(self, node):
        """
        Return True if list is a palindrome

        Use a stack to record the node values up to half way, then compare the stack with the
        second half.

        :param node: Head node of linked list
        :return: True if palindrome
        """
        stack = []
        p1 = node  # slow
        p2 = node  # fast

        while p2 is not None and p2.next is not None:
            stack.append(p1.val)
            p1 = p1.next
            p2 = p2.next.next

        if p2 is not None:
            # Odd number of nodes; we can ignore the centre node
            p1 = p1.next

        while p1 is not None:
            try:
                val = stack.pop()
            except IndexError:
                # Empty stack
                return False

            if p1.val != val:
                return False

            p1 = p1.next

        return True


testdata = [
    ((Node.from_array([0, 1, 2, 1, 0]),), True, does_not_raise()),
    ((Node.from_array([0, 1, 1, 0]),), True, does_not_raise()),
    ((Node.from_array([0]),), True, does_not_raise()),
    ((Node.from_array([0, 0]),), True, does_not_raise()),
    ((Node.from_array([0, 1]),), False, does_not_raise()),
    ((Node.from_array([0, 1, 2]),), False, does_not_raise()),
    ((Node.from_array([0, 1, 1, 3]),), False, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.is_palindrome(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
