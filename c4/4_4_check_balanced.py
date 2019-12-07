import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode


class Solution:
    class NotBalancedError(Exception):
        pass

    def is_balanced(self, node):
        """
        Return True if the depth of children at any node differs by more than 1.

        :param node: The node to check
        :return:
        """
        try:
            self.balanced_height_check(node)
        except self.NotBalancedError:
            return False
        return True

    def balanced_height_check(self, node):
        """
        Get the height of the tree. Also check that the tree is balanced.
        """
        if not node:
            return 0

        left_height = self.balanced_height_check(node.left)
        right_height = self.balanced_height_check(node.right)

        # Check balance
        if abs(left_height - right_height) > 1:
            raise self.NotBalancedError

        return max(left_height, right_height) + 1


testdata = [
    ((BinaryNode.from_array([1, 2, 3]),), True, does_not_raise()),
    ((BinaryNode.from_array([1, 2, None, 3]),), False, does_not_raise()),
    ((BinaryNode.from_array(range(100)),), True, does_not_raise()),
    ((BinaryNode.from_array([1, 2, None, 4, 5, 6, None, 7, None, None, None, None, None, None, None, 8]),),
     False, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.is_balanced(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
