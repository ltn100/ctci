import pytest
from contextlib import ExitStack as does_not_raise


class Box:
    def __init__(self, h, w, d):
        self.h = h
        self.w = w
        self.d = d

    def __repr__(self):
        return "{}x{}x{}".format(self.h, self.w, self.d)

    def __lt__(self, other):
        return self.h < other.h

    def will_stack_on(self, below):
        return below.h > self.h and below.w > self.w and below.d > self.d


class Solution:
    def get_height(self, boxes):
        """
        Given an array of boxes, calculate the maximum height that can be stacked,
        given that each box must be strictly smaller in all dimensions than the one
        below it.

        :param boxes: A list of boxes
        :return: The max height
        """
        boxes.sort(reverse=True)
        return self.get_height_helper(boxes, None, 0, {})

    def get_height_helper(self, boxes, bottom_idx, next_idx, memo):
        if next_idx >= len(boxes):
            return 0

        if bottom_idx is None or boxes[next_idx].will_stack_on(boxes[bottom_idx]):
            if next_idx in memo:
                height_inc_bottom = memo[next_idx]
            else:
                height_inc_bottom = boxes[next_idx].h
                height_inc_bottom += self.get_height_helper(boxes, next_idx, next_idx+1, memo)
                memo[next_idx] = height_inc_bottom
        else:
            height_inc_bottom = 0

        height_excl_bottom = self.get_height_helper(boxes, bottom_idx, next_idx+1, memo)

        return max(height_inc_bottom, height_excl_bottom)


testdata = [
    (([Box(1, 1, 1), Box(2, 2, 3), Box(3, 2, 5)],), 4, does_not_raise()),
    (([Box(1, 1, 1), Box(2, 2, 3), Box(3, 2, 5), Box(7, 8, 9), Box(2, 5, 6), Box(8, 4, 2)],), 11, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_height(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
