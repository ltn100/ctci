import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def multiply_iterative(self, a, b):
        """
        Return a*b

        :param a: positive integer
        :param b: positive integer
        :return: a * b
        """
        shift = 0
        while (a >> 1) + (a >> 1) == a:
            a >>= 1
            shift += 1

        while (b >> 1) + (b >> 1) == b:
            b >>= 1
            shift += 1

        result = 0
        for _ in range(min(a, b)):
            result += max(a, b)

        if shift:
            result <<= shift

        return result

    def multiply_recursive(self, a, b):
        return self.multiply_recursive_helper(min(a, b), max(a, b), {})

    def multiply_recursive_helper(self, smaller, larger, memo):
        if (smaller, larger) in memo:
            return memo[(smaller, larger)]

        if smaller == 0:
            return 0
        if smaller == 1:
            return larger

        if (smaller >> 1) + (smaller >> 1) == smaller:
            memo[(smaller, larger)] = self.multiply_recursive_helper(smaller >> 1, larger, memo) + \
                                      self.multiply_recursive_helper(smaller >> 1, larger, memo)
        elif (larger >> 1) + (larger >> 1) == larger:
            memo[(smaller, larger)] = self.multiply_recursive_helper(smaller, larger >> 1, memo) + \
                                      self.multiply_recursive_helper(smaller, larger >> 1, memo)
        else:
            memo[(smaller, larger)] = larger + self.multiply_recursive_helper(smaller-1, larger, memo)
        return memo[(smaller, larger)]

testdata = [
    ((3, 5), 3*5, does_not_raise()),
    ((1024, 1024), 1024*1024, does_not_raise()),
    ((1024, 1025), 1024*1025, does_not_raise()),
    ((1025, 1024), 1025*1024, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.multiply_iterative(*args) == res


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution2(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.multiply_recursive(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
