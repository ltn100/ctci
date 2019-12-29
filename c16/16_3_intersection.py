import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def intersection(self, a1, a2, b1, b2):
        """
        description

        :param arg:
        :return:
        """
        ix = 0
        if a2[0] - a1[0] == 0:
            ma = None
            ix = a1[0]
            ca = a1[1]
        else:
            ma = (a2[1] - a1[1])/(a2[0] - a1[0])
            ca = a1[1] - ma * a1[0]

        if b2[0] - b1[0] == 0:
            mb = None
            ix = b1[0]
            cb = b1[1]
        else:
            mb = (b2[1] - b1[1])/(b2[0] - b1[0])
            cb = b1[1] - mb * b1[0]

        if ma is not None and mb is not None:
            if ma - mb == 0:
                return None, None  # lines are parallel
            ix = (cb - ca)/(ma - mb)

        if ma is None and mb is None:
            return None, None  # lines are vertical and parallel

        if ma is not None:
            iy = ma * ix + ca
        elif mb is not None:
            iy = mb * ix + cb

        if a1[0] <= ix <= a2[0] and b1[0] <= ix <= b2[0] and a1[1] <= iy <= a2[1] and b1[1] <= iy <= b2[1]:
            return ix, iy
        else:
            return None, None


testdata = [
    (((2, 5), (9, 19), (2, 2), (8, 20)), (5, 11), does_not_raise()),
    (((2, 0), (2, 4), (0, 2), (4, 2)), (2, 2), does_not_raise()),
    (((2, 0), (2, 4), (2, 0), (2, 4)), (None, None), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.intersection(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
