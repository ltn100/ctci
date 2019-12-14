import pytest
from contextlib import ExitStack as does_not_raise
from bits import b2i


class Solution:
    def pairwise_swap(self, n):
        """
        Swap pairwise bits

        :param n: Integer
        :return: Swapped version
        """
        # Extract odd and even bits
        odd = n & 0x55555555
        even = n & 0xaaaaaaaa
        return odd << 1 | even >> 1


testdata = [
    ((b2i("01010101"),), b2i("10101010"), does_not_raise()),
    ((b2i("1"),), b2i("10"), does_not_raise()),
    ((b2i("110101000101"),), b2i("111010001010"), does_not_raise()),
    ((b2i("0"),), b2i("0"), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.pairwise_swap(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
