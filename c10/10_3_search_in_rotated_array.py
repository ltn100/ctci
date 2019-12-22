import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def search_rotated(self, arr, n):
        """
        description

        TODO: fix case where arr[0] == arr[-1]

        :param arg:
        :return:
        """
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == n:
                return mid
            if arr[mid] >= arr[0] and n <= arr[-1]:
                low = mid + 1
            else:
                if arr[mid] > n:
                    high = mid - 1
                else:
                    low = mid + 1

        return None


testdata = [
    (([15, 16, 18, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5), 8, does_not_raise()),
    (([15, 16, 18, 20, 25, 1, 3, 4, 5, 7, 10, 13, 14], 5), 8, does_not_raise()),
    (([7, 10, 13, 14, 15, 16, 18, 20, 25, 1, 3, 4, 5], 5), 12, does_not_raise()),
    (([10, 13, 14, 15, 16, 18, 20, 25, 1, 3, 4, 5, 7], 5), 11, does_not_raise()),
    (([10, 13, 14, 15, 16, 18, 20, 25, 1, 3, 4, 5, 7], 10), 0, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.search_rotated(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
