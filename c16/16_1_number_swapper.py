import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def swap(self, a, b):
        """
        Swap two numbers without a temporary variable
        """
        a ^= b
        b ^= a
        a ^= b
        return a, b


testdata = [
    ((1, 2), (2, 1), does_not_raise()),
    ((1, 1), (1, 1), does_not_raise()),
    ((-1, 2), (2, -1), does_not_raise()),
    ((0, 2), (2, 0), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.swap(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
