import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def parens(self, n):
        """
        Return all valid combinations of n parentheses.

        :param n: number of parentheses
        :return: Set of valid parens
        """
        if n == 0:
            return {""}

        prev_parens_set = self.parens(n-1)
        parens_set = set()
        for prev_parens in prev_parens_set:
            for i in range(len(prev_parens)):
                parens_set.add(prev_parens[:i] + "()" + prev_parens[i:])
            # Add at end
            parens_set.add(prev_parens + "()")
        return parens_set


testdata = [
    ((1,), {"()"}, does_not_raise()),
    ((2,), {"()()", "(())"}, does_not_raise()),
    ((3,), {"()()()", "((()))", "()(())", "(())()", "(()())"}, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.parens(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
