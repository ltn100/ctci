import pytest
from contextlib import ExitStack as does_not_raise
import math


class Solution:
    def get_first_floor(self, floors):
        """
        Given a number of floors, determine the optimal starting
        floor for the first egg drop. Subsequent drops for egg 1
        will be from floors with a gap size decrementing by 1 each drop.

        :param floors: The total number of floors
        :return: The optimal first floor to start from
        """
        # Solve x**2 + x - 2*floors
        x = math.floor((-1+math.sqrt(1+4*2*floors))/2)

        # If we cannot potentially cover all floors with the first egg, then
        # the drops per egg may not be balanced. Round up x to ensure this is
        # the case
        if (x+1)*x/2 < floors-1:
            x += 1

        return x

    @staticmethod
    def brute_force_optimal_first_floor(floors):
        min_drops = floors
        optimal_floor = None
        for floor in range(floors):
            drops = Solution.worst_case_num_drops(floor, floors)
            if drops <  min_drops:
                min_drops = drops
                optimal_floor = floor
        return optimal_floor

    @staticmethod
    def worst_case_num_drops(drop1_floor, floors):
        worst_case = 0
        for breaking_floor in range(floors):
            worst_case = max(worst_case, Solution.num_drops(drop1_floor, floors, breaking_floor))
        return worst_case

    @staticmethod
    def num_drops(drop1_floor, floors, breaking_floor):
        num_drops = 0
        floor = drop1_floor

        # Egg 1
        last_non_breaking_floor = -1
        while floor < floors:
            num_drops += 1
            if floor >= breaking_floor:
                break
            last_non_breaking_floor = floor
            floor += max(1, (drop1_floor - num_drops))

        first_breaking_floor = floor

        # Egg 2
        for floor in range(last_non_breaking_floor+1, first_breaking_floor):
            num_drops += 1
            if floor >= breaking_floor:
                break

        return num_drops

testdata = [
    ((100,), 14, does_not_raise()),
    ((100,), Solution.brute_force_optimal_first_floor(100), does_not_raise()),
    ((10,), Solution.brute_force_optimal_first_floor(10), does_not_raise()),
    ((62,), Solution.brute_force_optimal_first_floor(62), does_not_raise()),
    ((137,), Solution.brute_force_optimal_first_floor(137), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_first_floor(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
