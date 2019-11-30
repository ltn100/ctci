import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def rotate_matrix(self, mat):
        """
        Rotate matrix (list of lists) 90 degrees clockwise.

        Transpose and reverse rows.

        :param mat: Input matrix
        :return: Rotated matrix
        """
        if len(mat) == 0 or len(mat) != len(mat[0]):
            raise IndexError

        return [list(reversed(row)) for row in zip(*mat)]


class Solution2:
    def rotate_matrix(self, mat):
        """
        Rotate matrix (list of lists) 90 degrees clockwise.

        In-place solution. Do rotation in place in each layer recursively.

        :param mat: Input matrix
        :return: Rotated matrix
        """
        if len(mat) == 0 or len(mat) != len(mat[0]):
            raise IndexError

        n = len(mat)-1  # for brevity
        for layer in range(len(mat)//2):  # if odd num layers, the centre layer does not need to be touched
            for i in range(layer, n-layer):
                tmp = mat[layer][i]                     # top -> tmp
                mat[layer][i] = mat[n-i][layer]         # left -> top
                mat[n-i][layer] = mat[n-layer][n-i]     # bottom -> left
                mat[n-layer][n-i] = mat[i][n-layer]     # right -> bottom
                mat[i][n-layer] = tmp                   # tmp -> right

        return mat


testdata = [
    (([[1]],), [[1]], does_not_raise()),
    (([],), [], pytest.raises(IndexError)),
    (
        (
            [[1,2,3],
             [4,5,6],
             [7,8,9]],
        ),
        [[7,4,1],
         [8,5,2],
         [9,6,3]],
        does_not_raise()
    ),
    (
        (
            [[ 1, 2, 3, 4],
             [ 5, 6, 7, 8],
             [ 9,10,11,12],
             [13,14,15,16]],
        ),
        [[13, 9, 5, 1],
         [14,10, 6, 2],
         [15,11, 7, 3],
         [16,12, 8, 4]],
        does_not_raise()
    ),
    (([[1, 2]],), None, pytest.raises(IndexError)),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.rotate_matrix(*args) == res


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution2(args, res, expectation):
    with expectation:
        s = Solution2()
        assert s.rotate_matrix(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
