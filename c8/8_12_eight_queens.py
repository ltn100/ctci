import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def queen_pos(self, n):
        """
        description

        :param arg:
        :return:
        """
        return self.queen_pos_helper(4, [], [])

    def queen_pos_helper(self, n, queens, results):
        if len(queens) == n:
            results.append(queens)
            return results

        c = len(queens)
        for r in range(n):
            blocked = False
            for qr, qc in queens:
                if r == qr or c == qc or abs(qr - r) == abs(qc - c):
                    blocked = True
                    break

            if blocked:
                continue

            self.queen_pos_helper(n, queens+[(r, c)], results)

        return results

    def is_valid(self, queens):
        for r, c in queens:
            for qr, qc in queens:
                if r == qr and c == qc:
                    continue

                if r == qr or c == qc or abs(qr - r) == abs(qc - c):
                    return False

        return True


testdata = [
    ((4,), None, does_not_raise()),
    ((8,), None, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        for pos in s.queen_pos(*args):
            assert s.is_valid(pos)


if __name__ == '__main__':
    pytest.main(args=[__file__])
