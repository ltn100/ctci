import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode
from collections import Counter


class Solution:
    def paths_with_sum(self, root, k):
        """
        Return the number of paths within a tree that sum to a value k. The
        paths must only descend the tree, but can be from any node to any descendant
        node.

        This solution does a DFS through the tree, keeping track of the cumulative sum
        of the nodes since the root. The cumulative totals are insert into a hashmap. If
        the difference between the current cumulative sum minus k equals any of the previously
        calculated sums (in the hashmap) then there is a path to that previous node with total k.

        :param root: The root node of the tree
        :return: The path count
        """
        hashmap_init = {0: 1}  # There will always be one path to the first node
        return self.paths_with_sum_helper(root, k, Counter(hashmap_init), 0, 0)

    def paths_with_sum_helper(self, node, k, hashmap, cumsum, paths):
        if node is None:
            return paths

        cumsum += node.val
        hashmap[cumsum] += 1

        for part_sum, count in hashmap.items():
            if part_sum == cumsum - k:
                paths += count

        # dfs
        paths = self.paths_with_sum_helper(node.left, k, hashmap, cumsum, paths)
        paths = self.paths_with_sum_helper(node.right, k, hashmap, cumsum, paths)

        cumsum -= node.val
        hashmap[cumsum] -= 1

        return paths


tree = node = BinaryNode(10)
node.left = BinaryNode(5)
node = node.left
node.left = BinaryNode(1)
node = node.left
node.left = BinaryNode(2)
node.right = BinaryNode(2)
node = node.left
node.left = BinaryNode(-1)
node = node.leftnode = node.left
node.left = BinaryNode(-1)
node = node.left
node.right = BinaryNode(7)
node = node.right
node.left = BinaryNode(1)
node = node.left
node.left = BinaryNode(2)
testdata = [
    ((tree, 8), 6, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.paths_with_sum(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
