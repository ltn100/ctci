import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def sort_stack(self, stack):
        """
        Sort the stack, with the smallest item at the top, using only one other stack as
        a temporary buffer.

        Each element is popped from the stack, and placed on the temporary stack in reverse
        order (with largest at the top). We can put it in the correct order by using the original
        stack as a further temporary buffer.

        :param stack: The stack to be sorted
        :return: The sorted stack
        """
        temp_stack = []

        while stack:
            elem = stack.pop()
            while temp_stack and temp_stack[-1] > elem:
                # Move items off of temp stack to allow us to place
                # elem in the correct location (in reverse order)
                stack.append(temp_stack.pop())

            temp_stack.append(elem)

        # Move all items from temp_stack to stack
        while temp_stack:
            stack.append(temp_stack.pop())

        return stack


testdata = [
    (([1, 2, 3],), [3, 2, 1], does_not_raise()),
    (([1, 3, 2],), [3, 2, 1], does_not_raise()),
    (([3, 2, 1],), [3, 2, 1], does_not_raise()),
    (([1],), [1], does_not_raise()),
    (([],), [], does_not_raise()),
    (([3, 2, 7, 4, 5, -100, 9, 0, 6, 8, 1],), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -100], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.sort_stack(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
