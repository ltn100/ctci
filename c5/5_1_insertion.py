import pytest
from contextlib import ExitStack as does_not_raise
from bits import b2i


class Solution:
    def insert(self, n, m, i, j):
        """
        Given two integers, n and m. Insert the bits of m into n starting at
        bit index i and ending at bit index j.

        :param n: integer target
        :param m: integer to be inserted
        :param i: start index for insertion
        :param j: end index for insertion (inclusive)
        :return:
        """
        # Create mask to unset target bits
        mask = (2**(j-i+1))-1 << i

        # Clear bits in target
        n &= ~mask

        # Insert m into target
        n |= m << i

        return n


testdata = [
    ((1024, 19, 2, 6), 1100, does_not_raise()),
    ((b2i("10000000000"), b2i("10011"), 2, 6), b2i("10001001100"), does_not_raise()),
    ((b2i("11111111110"), b2i("10011"), 2, 7), b2i("11101001110"), does_not_raise()),
    ((b2i("0"), b2i("10011"), 2, 7), b2i("1001100"), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.insert(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
