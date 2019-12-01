import pytest
from contextlib import ExitStack as does_not_raise
from linkedlist import Node


class Solution:
    def delete_node(self, node, _head):
        """
        Delete a (central) node from a linked list, given only that node

        :param node: The node to delete
        :param _head: Only for testing purposes - do not touch!
        :return: None
        """
        node.val = node.next.val
        node.next = node.next.next

        return _head


LL = Node.from_array([1, 2, 3, 4, 5, 6, 7, 8, 9])
testdata = [
    ((LL.next.next, LL), Node.from_array([1, 2, 4, 5, 6, 7, 8, 9]), does_not_raise()),  # delete 3
    ((LL.next.next.next.next.next.next.next, LL), Node.from_array([1, 2, 4, 5, 6, 7, 9]), does_not_raise()),  # delete 8
    ((LL.next, LL), Node.from_array([1, 4, 5, 6, 7, 9]), does_not_raise()),  # delete 2
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.delete_node(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
