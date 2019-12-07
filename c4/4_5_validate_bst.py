import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode


class Solution:
    def is_valid_bst(self, root, min_val=float('-inf'), max_val=float('inf')):
        """
        Return True if tree is a valid BST.

        :param root: The root node
        :param min_val: The minimum value allowed in this tree (exclusive)
        :param max_val: The maximum value allowed in this tree (inclusive)
        :return: True if valid BST
        """
        if root is None:
            return True

        if root.val <= min_val:
            return False
        if root.val > max_val:
            return False
        if not self.is_valid_bst(root.left, min(min_val, root.val), root.val):
            return False
        if not self.is_valid_bst(root.right, root.val, max(max_val, root.val)):
            return False

        return True


testdata = [
    ((BinaryNode.from_array([2, 1, 3]),), True, does_not_raise()),
    ((BinaryNode.from_array([1, 2, 3]),), False, does_not_raise()),
    ((BinaryNode.from_array([3, 2, 1]),), False, does_not_raise()),
    ((BinaryNode.from_array([1]),), True, does_not_raise()),
    ((BinaryNode.from_array([20, 20]),), True, does_not_raise()),
    ((BinaryNode.from_array([20, None, 20]),), False, does_not_raise()),  # right values must be strictly greater
    ((BinaryNode.from_array([20, 10, 30, None, 25]),), False, does_not_raise()),
    ((BinaryNode.from_array([20, 10, 30, None, 20]),), True, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.is_valid_bst(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
