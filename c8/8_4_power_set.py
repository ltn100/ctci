import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def powerset(self, s):
        """
        Given a set, s, return all subsets of s.

        :param s:
        :return: set of sets
        """
        result = {frozenset(s)}  # need add frozensets, because sets of non-hashable (mutable) types are not allowed

        if len(s) == 0:
            return result

        for elem in s:
            residual = s - set(frozenset([elem]))
            result.update(self.powerset(residual))

        return result


testdata = [
    ((set(), ), {frozenset()}, does_not_raise()),
    (({1}, ), {frozenset(), frozenset([1])}, does_not_raise()),
    (({1, 2}, ), {frozenset(), frozenset([1]), frozenset([2]), frozenset([1, 2])}, does_not_raise()),
    (({1, 2, 3}, ), {frozenset(), frozenset([1]), frozenset([2]), frozenset([3]), frozenset([1, 2]),
                     frozenset([2, 3]), frozenset([1, 3]), frozenset([1, 2, 3])}, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.powerset(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
