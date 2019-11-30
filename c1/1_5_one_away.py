import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def one_away(self, s1, s2):
        """
        Return True if s2 is one (or zero) edits away from s1.

        If lengths are equal, edit must be an update.
        If s1 is longer, edit must be a insertion.
        If s1 is shorter, edit must be an deletion.

        :param s1: string 1
        :param s2: string 2
        :return: True if s1 is one or zero edits away from s2
        """
        edits = 0
        if len(s1) == len(s2):
            # Update
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    edits += 1
                    if edits > 1:
                        return False

        elif len(s1) == len(s2)+1:
            # Insertion
            for i in range(len(s2)):    # iterate over shorter of two
                if s1[i] != s2[i-edits]:
                    edits += 1
                    if edits > 1:
                        return False

        elif len(s1) == len(s2)-1:
            # Deletion
            for i in range(len(s1)):
                if s1[i-edits] != s2[i]:
                    edits += 1
                    if edits > 1:
                        return False
        else:
            return False

        return True

testdata = [
    (("pale", "ple"), True, does_not_raise()),
    (("pales", "pale"), True, does_not_raise()),
    (("pale", "bale"), True, does_not_raise()),
    (("pale", "bake"), False, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.one_away(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
