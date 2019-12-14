import pytest
from contextlib import ExitStack as does_not_raise
from bits import b2i


class Solution:
    def distance(self, a, b):
        """
        Return the number of bits that need to be changed to convert integer a to integer  b

        :param a: Integer
        :param b: Integer
        :return: Distance between a and b
        """
        xor = a ^ b
        count = 0
        while xor:
            count += xor & 1
            xor >>= 1
        return count


testdata = [
    ((b2i("11101"), b2i("01111")), 2, does_not_raise()),
    ((b2i("0"), b2i("0")), 0, does_not_raise()),
    ((b2i("1"), b2i("1")), 0, does_not_raise()),
    ((b2i("1"), b2i("0")), 1, does_not_raise()),
    ((b2i("1111111"), b2i("0")), 7, does_not_raise()),
    ((b2i("1111111"), b2i("1")), 6, does_not_raise()),
    ((b2i("10101010"), b2i("01010101")), 8, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.distance(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
