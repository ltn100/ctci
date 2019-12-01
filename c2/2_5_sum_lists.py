import pytest
from contextlib import ExitStack as does_not_raise
from linkedlist import Node


class Solution:
    def sum(self, l1, l2):
        """
        Given two linked lists, each storing a decimal number as single digits in reverse order, return
        sum of the two numbers as a third linked list

        :param l1: list of digits
        :param l2: list of digits
        :return: list of digits being the sum of l1 and l2
        """
        dummy_head = sum = Node()  # dummy node
        carry = 0
        while l1 is not None or l2 is not None or carry:
            digit = carry
            if l1 is not None:
                digit += l1.val
                l1 = l1.next
            if l2 is not None:
                digit += l2.val
                l2 = l2.next
            carry = digit // 10
            digit %= 10
            sum.next = Node(digit)
            sum = sum.next

        return dummy_head.next


class Solution2:
    def sum_reverse(self, l1, l2):
        # TODO
        pass


testdata = [
    ((Node.from_array([7, 1, 6]), Node.from_array([5, 9, 2])), Node.from_array([2, 1, 9]), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.sum(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
