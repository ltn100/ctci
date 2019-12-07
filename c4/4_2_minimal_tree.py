import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode


class Solution:
    def minimal_tree(self, arr):
        """
        Given a sorted array with unique integers, create a BST of minimal height.

        The midpoint of the array is inserted in the root, and then, recursively, the
        left and right trees are built the same way.

        :param arr: Sorted array
        :return: BST root node
        """
        if not arr:
            return None

        return self.minimal_tree_helper(arr, 0, len(arr))

    def minimal_tree_helper(self, arr, start, end):  # inclusive start, exclusive end
        if start >= end:
            return None

        # Split array
        mid_idx = (start + end) // 2

        node = BinaryNode(arr[mid_idx])
        node.left = self.minimal_tree_helper(arr, start, mid_idx)  # exclusive end
        node.right = self.minimal_tree_helper(arr, mid_idx+1, end)

        return node


testdata = [
    (([1, 2, 3],), (2, 2), does_not_raise()),
    (([1],), (1, 1), does_not_raise()),
    (([-1],), (1, -1), does_not_raise()),
    (([],), None, pytest.raises(TypeError)),
    ((list(range(2**3-1)),), (3, (2**3-1)//2), does_not_raise()),
    ((list(range(2**4-1)),), (4, (2**4-1)//2), does_not_raise()),
    ((list(range(2**4)),), (5, (2**4-1)//2+1), does_not_raise()),
    ((list(range(2**10-1)),), (10, (2**10-1)//2), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        res_height, res_mid_val = res
        s = Solution()
        bst = s.minimal_tree(*args)
        assert bst.height() == res_height
        assert bst.in_order() == args[0]
        assert bst.val == res_mid_val


if __name__ == '__main__':
    pytest.main(args=[__file__, "-s"])
