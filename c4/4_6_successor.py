import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode


class Solution:
    def get_successor(self, node):
        """
        Get the in-order successor to the given node. Can access node.parent.

        :param node: Binary tree node
        :return: The successor node
        """
        if node is None:
            return None

        if node.right:
            # If we have a right node, then we just need the leftmost leaf node from this child
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            # If we have no right node, then we need to ascend to a parent where we come from the left
            prev = node
            node = node.parent
            while node is not None and prev is not node.left:
                prev = node
                node = node.parent
            return node


tree = BinaryNode.from_array([20, 10, 30, 5, None, 21, 33, None, None, None, None, None, 25])
testdata = [
    ((tree,), 21, does_not_raise()),
    ((tree.left,), 20, does_not_raise()),  # 10
    ((tree.right.left.right,), 30, does_not_raise()),  # 25
    ((tree.right.right,), None, pytest.raises(AttributeError)),  # 33
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_successor(*args).val == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
