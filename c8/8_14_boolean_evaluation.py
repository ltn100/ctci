import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def num_ways(self, s, result, memo=None):
        """
        Given a string of boolean values and operations, return the number
        of different ways that parentheses can be added whilst still maintaining
        the desired result.

        :param s: string of boolean ops
        :param result: the desired result (bool)
        :param memo: memoization param
        :return:
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1 if bool(int(s)) == result else 0
        if memo is None:
            memo = {}
        if (s, result) in memo:
            return memo[(s, result)]

        num_ways = 0
        for i in range(1, len(s), 2):
            operator = s[i]
            left = s[:i]
            right = s[i+1:]
            if operator == '&':
                if result:
                    num_ways += self.num_ways(left, True, memo) * self.num_ways(right, True, memo)
                else:
                    num_ways += self.num_ways(left, True, memo) * self.num_ways(right, False, memo) + \
                                self.num_ways(left, False, memo) * self.num_ways(right, True, memo) + \
                                self.num_ways(left, False, memo) * self.num_ways(right, False, memo)
            if operator == '|':
                if result:
                    num_ways += self.num_ways(left, True, memo) * self.num_ways(right, False, memo) + \
                                self.num_ways(left, False, memo) * self.num_ways(right, True, memo) + \
                                self.num_ways(left, True, memo) * self.num_ways(right, True, memo)
                else:
                    num_ways += self.num_ways(left, False, memo) * self.num_ways(right, False, memo)
            if operator == '^':
                if result:
                    num_ways += self.num_ways(left, True, memo) * self.num_ways(right, False, memo) + \
                                self.num_ways(left, False, memo) * self.num_ways(right, True, memo)
                else:
                    num_ways += self.num_ways(left, True, memo) * self.num_ways(right, True, memo) + \
                                self.num_ways(left, False, memo) * self.num_ways(right, False, memo)

        memo[(s, result)] = num_ways

        return num_ways


testdata = [
    (("1^0|0|1", False), 2, does_not_raise()),
    (("0&0&0&1^1|0", True), 10, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.num_ways(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
