import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def move(self, result, src, dest):
        result.append("{}->{}".format(src, dest))

    def tower_of_hanoi(self, n):
        """
        Solve tower of hanoi

        :param arg:
        :return:
        """
        return self.tower_of_hanoi_helper(n, "A", "C", "B", [])

    def tower_of_hanoi_helper(self, n, src, dest, temp, result):
        if n == 0:
            return result

        self.tower_of_hanoi_helper(n-1, src, temp, dest, result)
        self.move(result, src, dest)
        self.tower_of_hanoi_helper(n-1, temp, dest, src, result)
        return result


testdata = [
    ((1,), ["A->C"], does_not_raise()),
    ((2,), ["A->B", "A->C", "B->C"], does_not_raise()),
    ((3,), ["A->C", "A->B", "C->B", "A->C", "B->A", "B->C", "A->C"], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.tower_of_hanoi(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
