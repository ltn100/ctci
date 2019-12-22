import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def missing_int(self, arr, size):
        """
        description

        :param arg:
        :return:
        """
        ba = bytearray((size//8)+1)
        for n in arr:
            byte = n // 8
            offset = n % 8
            ba[byte] |= 1 << offset

        for byte in range((size//8)+1):
            if ba[byte] < 0xFF:
                for offset in range(8):
                    if (ba[byte] >> offset) & 1 == 0:
                        return byte * 8 + offset


testdata = [
    ((list(range(1000))+list(range(1001, 2000)), 2000), 1000, does_not_raise()),
    ((list(range(2000)), 2000), 2000, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.missing_int(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
