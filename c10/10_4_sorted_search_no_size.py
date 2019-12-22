import pytest
from contextlib import ExitStack as does_not_raise


class Listy:
    def __init__(self, arr):
        self.arr = arr

    def __getitem__(self, key):
        if 0 <= key < len(self.arr):
            return self.arr[key]
        else:
            return -1


class Solution:
    def search(self, lst, n):
        """
        description

        :param arg:
        :return:
        """
        i = 0
        while True:
            idx = (2**i) - 1
            if lst[idx] == n:
                # Got lucky
                return idx
            if lst[idx] < 0 or lst[idx] > n:
                break
            i += 1

        if i < 1:
            # Not found
            return None

        # Perform (fairly) normal binary search
        high = (2**i) - 1
        low = (2**(i-1)) - 1
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] == n:
                return mid
            if lst[mid] == -1 or lst[mid] > n:
                high = mid - 1
            else:
                low = mid + 1

        # Not found
        return None


testdata = [
    ((Listy([1, 3, 4, 6, 7, 23, 23, 25, 33, 54, 76, 123, 132]), 25), 7, does_not_raise()),
    ((Listy([1]*10+[2]+[3]*100), 2), 10, does_not_raise()),
    ((Listy([1]), 1), 0, does_not_raise()),
    ((Listy([1]), 2), None, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.search(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
