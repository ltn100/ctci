import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode


class Solution:
    def is_subtree(self, t1, t2):
        """
        Return True if t2 is a subtree of t1

        :param t1: Tree 1 (larger)
        :param t2: Tree 2 (smaller)
        :return: True if t2 is a subtree of t1
        """
        if t2 is None:
            return True
        if t1 is None:
            return False
        if t1.val == t2.val:
            return self.is_same_tree(t1, t2)
        if self.is_subtree(t1.left, t2) or self.is_subtree(t1.right, t2):
            return True
        return False

    def is_same_tree(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        return self.is_same_tree(t1.left, t2.left) and self.is_same_tree(t1.right, t2.right)


testdata = [
    ((BinaryNode.from_array([1, 2, 3]), BinaryNode.from_array([3])), True, does_not_raise()),
    ((BinaryNode.from_array([1, 2, 3]), BinaryNode.from_array([4])), False, does_not_raise()),
    ((BinaryNode.from_array([1, 2, 3, 4]), BinaryNode.from_array([2, 4])), True, does_not_raise()),
    ((BinaryNode.from_array([1, 2, 3, 4]), BinaryNode.from_array([2, 4, 5])), False, does_not_raise()),
    ((BinaryNode.from_array([range(10)]), BinaryNode.from_array([range(10)])), True, does_not_raise()),
    ((BinaryNode.from_array([range(11)]), BinaryNode.from_array([range(10)])), False, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.is_subtree(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
