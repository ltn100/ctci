import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode


class Solution:
    def paths_with_sum(self, root, k):
        """
        Return the number of paths within a tree that sum to a value k. The
        paths must only descend the tree, but can be from any node to any descendant
        node.

        :param root: The root node of the tree
        :return: The path count
        """
        return 5


tree = node = BinaryNode(10)
node.left = BinaryNode(5)
node = node.left
node.left = BinaryNode(1)
node = node.left
node.left = BinaryNode(2)
node = node.left
node.left = BinaryNode(-1)
node = node.leftnode = node.left
node.left = BinaryNode(-1)
node = node.left
node.left = BinaryNode(7)
node = node.left
node.left = BinaryNode(1)
node = node.left
node.left = BinaryNode(2)
testdata = [
    ((tree, 8), 5, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.paths_with_sum(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
