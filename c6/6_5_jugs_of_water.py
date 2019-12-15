import pytest
from contextlib import ExitStack as does_not_raise


class Jug:
    def __init__(self, capacity):
        self.capacity = capacity
        self.quantity = 0

    def __repr__(self):
        return str(self.quantity)

    def fill(self, source=None):
        if source:
            source_vol = source.empty()
            space = self.capacity - self.quantity
            if source_vol > space:
                self.quantity = self.capacity
                source.quantity = source_vol - space
            else:
                self.quantity = source_vol
        else:
            # Fill from unlimited source
            self.quantity = self.capacity

    def empty(self):
        out = self.quantity
        self.quantity = 0
        return out

    def get_quantity(self):
        return self.quantity


class Solution:
    def get_4(self, j5, j3):
        """
        Given a 5 and 3-quart jugs, measure out 4 quarts.

        :param j5: 5-quart jug
        :param j3: 3-quart jug
        :return: A jug with 4 quarts in it
        """
        j5.fill()
        j3.fill(source=j5)  # j5 left with 2
        j3.empty()
        j3.fill(source=j5)
        j5.fill()
        j3.fill(source=j5)  # j5 left with 4
        return j5


testdata = [
    ((Jug(5), Jug(3)), 4, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_4(*args).get_quantity() == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
