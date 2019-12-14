import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def get_next(self, n):
        """
        Given a positive integer, return the next smallest and next largest numbers
        that have the same number of '1's in their binary representation.

        :param n: Positive integer
        :return: (s, l) tuple of next smallest and next largest numbers
        """
        return self.get_next_smaller(n), self.get_next_larger(n)

    def get_next_larger(self, n):
        # Find rightmost non-trailing zero
        found1, zero_idx = False, 0
        for i in range(32):
            bit = n & 1 << i
            if found1:
                if not bit:
                    zero_idx = i
                    break
            else:
                found1 = bool(bit)

        # Count 1s to the right of zero_idx
        num_ones = 0
        for i in range(zero_idx):
            bit = n & 1 << i
            if bit:
                num_ones += 1

        # Flip rightmost zero
        n |= 1 << zero_idx

        # Unset all bits to the right of that
        n &= ~((1 << zero_idx) - 1)

        # Add smallest int with the appropriate number of ones
        n |= (1 << (num_ones-1)) - 1

        return n

    def get_next_smaller(self, n):
        # Find rightmost non-trailing one
        found0, one_idx = False, 0
        for i in range(32):
            bit = n & 1 << i
            if found0:
                if bit:
                    one_idx = i
                    break
            else:
                found0 = not bool(bit)

        # Count 1s to the right of one_idx
        num_ones = 0
        for i in range(one_idx):
            bit = n & 1 << i
            if bit:
                num_ones += 1

        # Flip rightmost one
        n &= ~(1 << one_idx)

        # Unset all bits to the right of that
        n &= ~((1 << one_idx) - 1)

        # Add largest int with the appropriate number of ones
        n |= ((1 << (num_ones+1)) - 1) << (one_idx-num_ones-1)

        return n


testdata = [
    ((13948,), (13946, 13967), does_not_raise()),
    ((2,), (1, 4), does_not_raise()),
    ((30,), (29, 39), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_next(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
