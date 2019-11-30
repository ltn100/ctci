import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def zero_matrix(self, mat):
        """
        If an element in the matrix is zero, set its entire row and column to zero.

        Perform in-place.

        Use two variables to note whether the first row and/or column should be zeroed. Then
        use the first row to mark whether columns should be zeroed, and first column to mark
        whether rows

        :param mat: Input matrix
        :return: Zeroed matrix
        """
        if len(mat) == 0 or len(mat[0]) == 0:
            return mat

        zero_in_first_col = False
        for r in range(len(mat)):
            if mat[r][0] == 0:
                zero_in_first_col = True
                break

        zero_in_first_row = False
        for c in range(len(mat[0])):
            if mat[0][c] == 0:
                zero_in_first_row = True
                break

        for r in range(1, len(mat)):
            for c in range(1, len(mat[0])):
                if mat[r][c] == 0:
                    mat[0][c] = 0
                    mat[r][0] = 0

        # Zero the rows
        for r in range(len(mat)):
            if mat[r][0] == 0:
                for c in range(1, len(mat[0])):
                    mat[r][c] = 0

        # Zero the columns
        for c in range(len(mat[0])):
            if mat[0][c] == 0:
                for r in range(1, len(mat)):
                    mat[r][c] = 0

        if zero_in_first_row:
            for c in range(len(mat[0])):
                mat[0][c] = 0

        if zero_in_first_col:
            for r in range(len(mat)):
                mat[r][0] = 0

        return mat


testdata = [
    (
        (
            [[ 1, 0, 3, 4],
             [ 5, 6, 7, 8]],
        ),
        [[ 0, 0, 0, 0],
         [ 5, 0, 7, 8]],
        does_not_raise()
    ),
    (
        (
            [[ 1, 0, 3, 4],
             [ 5, 6, 7, 8],
             [ 9,10,11,12],
             [13,14, 0,16]],
        ),
        [[ 0, 0, 0, 0],
         [ 5, 0, 0, 8],
         [ 9, 0, 0,12],
         [ 0, 0, 0, 0]],
        does_not_raise()
    ),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.zero_matrix(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
