import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def get_magic_index(self, arr):
        """
        Given an array of sorted integers, return the index where arr[i] == i

        :param arr: Sorted array
        :return: Magic index
        """
        return self.get_magic_index_helper(arr, 0, len(arr))

    def get_magic_index_helper(self, arr, start, end, unique=False):
        if start >= end:
            return None

        mid = (start+end)//2

        if arr[mid] == mid:
            return mid

        if unique:
            if arr[mid] > mid:
                return self.get_magic_index_helper(arr, start, mid)
            else:
                return self.get_magic_index_helper(arr, mid+1, end)
        else:
            left = self.get_magic_index_helper(arr, start, mid)
            if left is not None:
                return left
            else:
                return self.get_magic_index_helper(arr, mid+1, end)


testdata = [
    (([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13],), 7, does_not_raise()),
    (([0, 1, 2],), 1, does_not_raise()),
    (([-1, 0, 1, 4],), None, does_not_raise()),
    (([-10, -5, 2],), 2, does_not_raise()),
    (([-10, -5, 0, 3],), 3, does_not_raise()),
    (([0, 3, 10, 11],), 0, does_not_raise()),
    (([-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13],), 2, does_not_raise()),
    (([-10, -5, -3, -2, -1, 6, 7, 7, 9, 12, 13],), 7, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_magic_index(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
