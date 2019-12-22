import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def sorted_merge(self, a, b):
        """
        Given two sorted arrays, with enough space in 'a' to accomodate 'b', merge the
        two lists into a.

        :param a: list a
        :param b: list b
        :return: list a
        """
        len_a = sum(map(lambda x: 0 if x is None else 1, a))
        end = len_a + len(b) - 1
        end_a = len_a - 1
        end_b = len(b) - 1
        while end_b >= 0:
            if end_a >= 0 and a[end_a] > b[end_b]:
                a[end_a], a[end] = a[end], a[end_a]
                end_a -= 1
            else:
                b[end_b], a[end] = a[end], b[end_b]
                end_b -= 1
            end -= 1

        return a


testdata = [
    (([1, 3, 5, 7, None, None, None], [2, 4, 6]), [1, 2, 3, 4, 5, 6, 7], does_not_raise()),
    (([1, 3, 5, 7, None, None, None, None], [2, 4, 6]), [1, 2, 3, 4, 5, 6, 7, None], does_not_raise()),
    (([2, 2, 2, 2, None, None, None, None], [1, 1, 1]), [1, 1, 1, 2, 2, 2, 2, None], does_not_raise()),
    (([1, 1, 1, 1, None, None, None, None], [1, 1, 1]), [1, 1, 1, 1, 1, 1, 1, None], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.sorted_merge(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
