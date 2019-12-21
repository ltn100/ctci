import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def triple_step_combinations(self, n):
        """
        Given a number of steps, n, get all the possible combinations of ways to climb
        the steps using 1, 2 or 3 stairs at a time.

        :param n: total number of steps
        :return: list of lists of integers 1--3.
        """
        res = []
        if n == 0:
            return res

        steps = self.triple_step_combinations(n-1)
        for step in steps:
            if step + [1] not in res:
                res.append(step + [1])
            if [1] + step not in res:
                res.append([1] + step)

        if n <= 3:
            res.append([n])

        return res

    def triple_step_num_ways(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.triple_step_num_ways(n-1) + self.triple_step_num_ways(n-2) + self.triple_step_num_ways(n-3)


testdata = [
    ((1,), [[1]], does_not_raise()),
    ((2,), [[1, 1], [2]], does_not_raise()),
    ((3,), [[1, 1, 1], [2, 1], [1, 2], [3]], does_not_raise()),
    ((4,), [[1, 1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [2, 2], [3, 1], [1, 3]], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        #print(s.triple_step_combinations(*args))
        #assert s.triple_step_combinations(*args) == res  # TODO: fix this
        assert s.triple_step_num_ways(*args) == len(res)


if __name__ == '__main__':
    pytest.main(args=[__file__])
