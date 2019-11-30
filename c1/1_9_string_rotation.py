import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def is_rotation(self, s1, s2):
        """
        Return true if s2 is a rotation of s1.

        :param s1: string 1
        :param s2: string 2
        :return: True if s2 is a rotation of s1
        """
        if len(s1) != len(s2):
            return False

        return self.is_substring(s1+s1, s2)

    def is_substring(self, s1, s2):
        """
        Return true if s2 is a substring of s1. Must only be called once.
        """
        return s2 in s1


testdata = [
    (("waterbottle", "erbottlewat"), True, does_not_raise()),
    (("a", "a"), True, does_not_raise()),
    (("a", "b"), False, does_not_raise()),
    (("aa", "ab"), False, does_not_raise()),
    (("a", "ab"), False, does_not_raise()),
    (("a", "aa"), False, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.is_rotation(*args) == res


def test_is_substring():
    s = Solution()
    assert s.is_substring("acara", "car")
    assert s.is_substring("car", "car")
    assert s.is_substring("cara", "car")
    assert s.is_substring("acar", "car")
    assert not s.is_substring("acara", "carb")

if __name__ == '__main__':
    pytest.main(args=[__file__])
