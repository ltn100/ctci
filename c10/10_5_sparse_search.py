import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def sparse_search(self, sparse, s):
        """
        description

        :param arg:
        :return:
        """
        low = 0
        high = len(sparse) - 1
        while low <= high:
            mid = (low + high) // 2

            # Move mid nearest non-empty string
            if sparse[mid] == "":
                i = 1
                while True:
                    if 0 <= mid+i < len(sparse) and sparse[mid+i] != "":
                        mid += i
                        break
                    if 0 <= mid-i < len(sparse) and sparse[mid-i] != "":
                        mid -= i
                        break
                    if mid-1 < 0 and mid+i >= len(sparse):
                        return None
                    i += 1

            if sparse[mid] == s:
                return mid
            if sparse[mid] < s:
                low = mid + 1
            else:
                high = mid - 1

        # Not found
        return None


testdata = [
    ((["at", "", "", "", "", "", "ball", "", "", "", "", "", "car", "", "", "dad", "", ""], "ball"), 6, does_not_raise()),
    ((["at", "", "", "", "", "", "ball", "", "", "", "", "", "car", "", "", "dad", "", ""], "at"), 0, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.sparse_search(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
