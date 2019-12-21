import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def perms(self, s):
        """
        description

        :param arg:
        :return:
        """
        perms = {s}
        for i in range(len(s)):
            c = s[i]
            for perm in self.perms(s[:i]+s[i+1:]):
                perms.add(c+perm)
        return perms


testdata = [
    (("ab",), {"ab", "ba"}, does_not_raise()),
    (("abc",), {"abc", "acb", "bac", "bca", "cab", "cba"}, does_not_raise()),
    (("abb",), {"abb", "bab", "bba"}, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.perms(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
