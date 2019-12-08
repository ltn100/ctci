import pytest
from contextlib import ExitStack as does_not_raise
from graph import BinaryNode


class Solution:
    def get_sequences(self, root):
        """
        Given a BST, return all possible sequences of insertion that could have led
        to the tree.

        :param root: Root node of BST
        :return: List of lists
        """
        if root is None:
            return [[]]

        ssl = self.get_sequences(root.left)
        ssr = self.get_sequences(root.right)

        woven = self.weave_lists_of_sequences(ssl, ssr)

        # Prepend val
        result = []
        for seq in woven:
            result.append([root.val] + seq)

        return result

    def weave_lists_of_sequences(self, ss1, ss2):
        result = []
        for s1 in ss1:
            for s2 in ss2:
                result.extend(self.weave_sequences(s1, s2))
        return result

    def weave_sequences(self, s1, s2):
        if not s1:
            return [s2]
        if not s2:
            return [s1]

        result = []
        partial_seqs = self.weave_sequences(s1[1:], s2)
        for partial_seq in partial_seqs:
            result.append([s1[0]] + partial_seq)

        partial_seqs = self.weave_sequences(s1, s2[1:])
        for partial_seq in partial_seqs:
            result.append([s2[0]] + partial_seq)

        return result


testdata = [
    ((BinaryNode.from_array([2, 1, 3]),), [[2, 1, 3], [2, 3, 1]], does_not_raise()),
    ((BinaryNode.from_array([2, 1, 3, 0]),), [[2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 1, 0]], does_not_raise()),
    ((BinaryNode.from_array([2, 1, 3, None, None, None, 4]),), [[2, 1, 3, 4], [2, 3, 1, 4], [2, 3, 4, 1]], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_sequences(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
