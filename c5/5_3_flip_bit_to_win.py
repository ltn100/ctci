import pytest
from contextlib import ExitStack as does_not_raise
from bits import b2i


class Solution:
    def longest_sequence(self, n):
        """
        Given an integer, find the longest sequence of 1s, given that you can flip
        exactly one bit.

        :param n: Integer
        :return: Length of sequence
        """
        curr = 0
        prev = 0
        longest = 1
        while n > 0:
            lsb = n & 1
            n >>= 1
            if lsb:
                curr += 1
                longest = max(longest, curr + prev + 1)
            else:
                prev = curr
                curr = 0

        return longest


testdata = [
    ((b2i("11011101111"),), 8, does_not_raise()),
    ((b2i("0"),), 1, does_not_raise()),
    ((b2i("1"),), 2, does_not_raise()),
    ((b2i("1111"),), 5, does_not_raise()),
    ((b2i("10000"),), 2, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.longest_sequence(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
