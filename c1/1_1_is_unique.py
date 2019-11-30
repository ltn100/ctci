import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def is_unique(self, s):
        """
        Return True if string s has all unique characters.

        Create hashset of characters and check that no characters have been
        seen before.

        :param s: input string
        :return: True if all unique
        """
        if len(s) > 128:
            return False

        seen = set()
        for c in s:
            if c in seen:
                return False
            seen.add(c)
        return True


class Solution2:
    def is_unique(self, s):
        """
        Return True if string s has all unique characters.

        Create bit array of characters and check that no characters have been
        seen before.

        :param s: input string
        :return: True if all unique
        """
        if len(s) > 128:
            return False

        # Use int as bit array
        seen = 0
        for c in s:
            mask = 1 << ord(c)
            if seen & mask:
                return False
            seen |= mask
        return True


testdata = [
    (("apeoij4u",), True, does_not_raise()),
    (("ap{!£*^$()]eo~@:ij4u",), True, does_not_raise()),
    (("z",), True, does_not_raise()),
    (("",), True, does_not_raise()),
    (("abcdefghijklmnopqrstuvwxyz",), True, does_not_raise()),
    (("aa",), False, does_not_raise()),
    (("abcdefghijklmnopqrstuvwxya",), False, does_not_raise()),
    (("a"*129,), False, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.is_unique(*args) == res


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution2(args, res, expectation):
    with expectation:
        s = Solution2()
        assert s.is_unique(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
