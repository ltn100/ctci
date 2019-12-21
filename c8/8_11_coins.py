import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def num_ways(self, cents, coins=None):
        """
        description

        :param arg:
        :return:
        """
        if coins is None:
            coins = [1, 5, 10, 25]

        if len(coins) == 1:
            return 1

        num_ways = 0
        largest_coin = coins.pop()
        while cents >= largest_coin:
            num_ways += self.num_ways(cents, coins[:])
            cents -= largest_coin
        num_ways += self.num_ways(cents, coins[:])

        return num_ways


testdata = [
    ((1,), 1, does_not_raise()),
    ((5,), 2, does_not_raise()),
    ((13,), 4, does_not_raise()),
    ((25,), 13, does_not_raise()),
    ((77,), 121, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.num_ways(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
