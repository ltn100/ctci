import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def find_dups(self, arr, max_n):
        """
        description

        :param arg:
        :return:
        """
        result = []
        ba = bytearray((max_n // 8) + 1)
        for n in arr:
            byte = n // 8
            offset = n % 8

            # check bit
            if (ba[byte] >> offset) & 1 == 0:
                # set bit
                ba[byte] |= 1 << offset
            else:
                # dupe
                result.append(n)

        return result


testdata = [
    (([1, 2, 2, 3, 7, 4, 10, 3, 7, 12], 32000), [2, 3, 7], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.find_dups(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
