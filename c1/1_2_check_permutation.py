import pytest
import collections
from contextlib import ExitStack as does_not_raise


class Solution:
    def check_permutation(self, s1, s2):
        """
        Return True if s1 is a permutation of s2

        First check lengths are equal, then create hashmap of counters to count
        chars in s1. Decrement counters when iterating s2.

        :param s1: string
        :param s2: string
        :return: True if s1 is a permutation of s2
        """
        if len(s1) != len(s2):
            return False

        counter = collections.Counter()
        for c in s1:
            counter[c] += 1
        for c in s2:
            counter[c] -= 1
            if counter[c] < 0:
                return False

        # As strings are same length, we can assume all counters are zero
        return True


testdata = [
    (("abc", "cba"), True, does_not_raise()),
    (("basiparachromatin", "marsipobranchiata"), True, does_not_raise()),
    (("a", "a"), True, does_not_raise()),
    (("aaaaaaaa", "aaaaaaaa"), True, does_not_raise()),
    (("", ""), True, does_not_raise()),
    (("true", "fals"), False, does_not_raise()),
    (("true", "false"), False, does_not_raise()),
    (("aaaaaaa", "aaaaaaaa"), False, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.check_permutation(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
