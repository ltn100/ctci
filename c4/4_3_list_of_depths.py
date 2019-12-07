import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode
from collections import deque


class Solution:
    def get_list_at_each_depth(self, root):
        """
        Produce a list of values at each depth.

        :param root: The root of a binary tree
        :return: A list of lists
        """
        queue = deque()
        queue.appendleft((root, 0))
        output = []
        while queue:
            node, level = queue.pop()
            if node is None:
                continue

            if len(output) <= level:
                output.append([])

            output[level].append(node.val)
            queue.appendleft((node.left, level+1))
            queue.appendleft((node.right, level+1))

        return output


testdata = [
    ((BinaryNode.from_array([1, 2, 3, None, None, None, 4]),), [[1], [2, 3], [4]], does_not_raise()),
    ((BinaryNode.from_array([1]),), [[1]], does_not_raise()),
    ((BinaryNode.from_array([]),), [], does_not_raise()),
    ((BinaryNode.from_array(range(10)),), [[0], [1, 2], [3, 4, 5, 6], [7, 8, 9]], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_list_at_each_depth(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
