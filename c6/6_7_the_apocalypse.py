import pytest
from contextlib import ExitStack as does_not_raise
import random


class Solution:
    def get_gender_ratio(self, n):
        """
        Get the gender ratio across n families

        :param n: Number of families
        :return: Ratio of girls to boys
        """
        boys = 0
        girls = 0
        for _ in range(n):
            while True:
                if random.choice([0, 1]) == 0:
                    girls += 1
                    break
                else:
                    boys += 1

        return girls / (girls+boys)


testdata = [
    ((1000,), 0.5, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_gender_ratio(*args) == pytest.approx(res, 0.05)


if __name__ == '__main__':
    pytest.main(args=[__file__])
