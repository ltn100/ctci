import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def search(self, matrix, val):
        """
        Given a maxrix, whose rows and columns are sorted integers, search for the
        value val.

        :param matrix: List of lists of ints
        :return: (r, c) coordinates
        """
        if len(matrix) == 0:
            return None, None

        return self.search_helper(matrix, val, 0, len(matrix)-1, 0, len(matrix[0])-1)

    def search_helper(self, matrix, val, min_r, max_r, min_c, max_c):
        if min_r > max_r or min_c > max_c:
            return None, None

        low_r = min_r
        high_r = max_r
        low_c = min_c
        high_c = max_c

        while low_r <= high_r or low_c <= high_c:
            mid_r = (low_r + high_r) // 2
            mid_c = (low_c + high_c) // 2
            if matrix[mid_r][mid_c] == val:
                return mid_r, mid_c
            if matrix[mid_r][mid_c] < val:
                if low_r <= high_r:
                    low_r = mid_r + 1
                if low_c <= high_c:
                    low_c = mid_c + 1
            else:
                if low_r <= high_r:
                    high_r = mid_r - 1
                if low_c <= high_c:
                    high_c = mid_c - 1

        # Search upper right
        r, c = self.search_helper(matrix, val, min_r, high_r, low_c, max_c)
        if r is not None:
            return r, c

        # Search lower left
        r, c = self.search_helper(matrix, val, low_r, max_r, min_c, high_c)
        if r is not None:
            return r, c

        return None, None


M = [
    [-100, -50, -20,  0,  1,  3, 10, 11],
    [-80,  -49, -19,  1,  2,  7, 12, 18],
    [-51,  -23,   5, 10, 11, 12, 13, 19],
    [-9,   -3,   15, 20, 31, 40, 43, 50],
    [1,     7,   10, 21, 32, 41, 51, 53],
    [2,     8,   12, 21, 32, 50, 60, 60],
    [4,     8,   14, 32, 33, 52, 65, 70]
]

testdata = [
    (([[1, 2, 3], [2, 2, 5], [4, 9, 10]], 9), (2, 1), does_not_raise()),
    ((M, 13), (2, 6), does_not_raise()),
    ((M, 8), (6, 1), does_not_raise()),
    ((M, 70), (6, 7), does_not_raise()),
    ((M, -100), (0, 0), does_not_raise()),
    ((M, 11), (0, 7), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.search(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
