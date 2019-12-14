import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def is_power_of_two(self, n):
        """
        Return true if the number is a power of two

        :param n: Integer
        :return: True if power of 2
        """
        return (n & (n-1)) == 0


testdata = [
    ((4,), True, does_not_raise()),
    ((1024,), True, does_not_raise()),
    ((31,), False, does_not_raise()),
    ((0,), True, does_not_raise()),
    ((1,), True, does_not_raise()),
    ((2**42,), True, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.is_power_of_two(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
