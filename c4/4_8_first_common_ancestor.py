import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode


class Solution:
    def get_first_common_ancestor(self, n1, n2):
        """
        Get the first common ancestor of two nodes. Can access node.parent.

        This approach is similar to finding the intersection node in two linked lists (2.7)

        :param n1: Node 1
        :param n2: Node 2
        :return: The common ancestor node, or None
        """
        if n1 is None or n2 is None:
            return None

        # get depth of each node
        tail1, depth1 = n1, 1
        while tail1.parent is not None:
            tail1 = tail1.parent
            depth1 += 1

        tail2, depth2 = n2, 1
        while tail2.parent is not None:
            tail2 = tail2.parent
            depth2 += 1

        if tail1 is not tail2:
            # Different trees
            return None

        # Move nodes to match lengths
        while depth1 > depth2:
            n1 = n1.parent
            depth1 -= 1

        while depth2 > depth1:
            n2 = n2.parent
            depth2 -= 1

        while n1 is not None and n2 is not None:
            if n1 is n2:
                return n1
            n1 = n1.parent
            n2 = n2.parent

        # Should never get here
        raise RuntimeError("n1 {} and n2 {} did something strange".format(n1, n2))


tree = BinaryNode.from_array([20, 10, 30, 5, None, 21, 33, None, None, None, None, None, 25])
testdata = [
    ((tree, tree), 20, does_not_raise()),
    ((tree, tree.left), 20, does_not_raise()),
    ((tree.left, tree.left.left), 10, does_not_raise()),
    ((tree.right.left.right, tree.left.left), 20, does_not_raise()),
    ((tree, None), None, pytest.raises(AttributeError)),
    ((tree.right.left.right, BinaryNode.from_array([20, 10, 30])), None, pytest.raises(AttributeError)),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_first_common_ancestor(*args).val == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
