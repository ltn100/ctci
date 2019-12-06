import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def problem(self, arg):
        """
        description

        :param arg:
        :return:
        """
        pass


testdata = [
    (("arg",), None, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.problem(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
