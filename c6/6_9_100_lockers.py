import pytest
from contextlib import ExitStack as does_not_raise
import math


class Solution:
    def get_num_open(self, n):
        """
        Given a number of lockers, n, get the number of open lockers after they have been
        cycled in multiples of 1-n.

        Only perfect squares will be left, so calculate the floor of sqrt(n)

        :param n: Number of lockers
        :return: The number left open
        """
        return math.floor(math.sqrt(n))

    @staticmethod
    def simulate(n):
        lockers = [0]*n  # start closed
        for i in range(n):
            for j in range(i, n, i+1):
                lockers[j] ^= 1  # cycle
        return sum(lockers)


testdata = [
    ((100,), 10, does_not_raise()),
    ((100,), Solution.simulate(100), does_not_raise()),
    ((10,), Solution.simulate(10), does_not_raise()),
    ((1000,), Solution.simulate(1000), does_not_raise()),
    ((2491,), Solution.simulate(2491), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_num_open(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
