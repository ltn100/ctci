import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def make_peaks(self, arr):
        """
        description

        :param arg:
        :return:
        """
        for i in range(1, len(arr)-1, 2):
            max_i = self.get_max_idx(arr, i-1, i, i+1)
            if max_i == i:
                continue
            arr[i], arr[max_i] = arr[max_i], arr[i]
        return arr

    def get_max_idx(self, arr, i, j, k):
        if arr[i] > arr[j] and arr[i] > arr[k]:
            return i
        if arr[j] > arr[i] and arr[j] > arr[k]:
            return j
        if arr[k] > arr[i] and arr[k] > arr[j]:
            return k


testdata = [
    (([5, 3, 1, 2, 3],), [3, 5, 1, 3, 2], does_not_raise()),
    (([1, 2, 3, 4, 5, 6, 7, 8],), [1, 3, 2, 5, 4, 7, 6, 8], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.make_peaks(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
