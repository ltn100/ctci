import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    NEIGHBOURS = [
        [-1, 0],  # Up
        [1, 0],   # Down
        [0, -1],  # Left
        [0, 1]    # Right
    ]

    def fill(self, screen, r, c):
        """
        description

        :param arg:
        :return:
        """
        return self.fill_helper(screen, r, c, set())

    def fill_helper(self, screen, r, c, visited):
        if r < 0 or r >= len(screen) or c < 0 or c >= len(screen[r]) or (r, c) in visited or screen[r][c] == 1:
            return screen

        visited.add((r, c))
        screen[r][c] = 1
        for neighbour in self.NEIGHBOURS:
            nr = r + neighbour[0]
            nc = c + neighbour[1]
            self.fill_helper(screen, nr, nc, visited)

        return screen


testdata = [
    (([[0, 0], [0, 0]], 0, 0), [[1, 1], [1, 1]], does_not_raise()),
    (([[0, 0, 0], [0, 1, 1], [0, 1, 0]], 0, 0), [[1, 1, 1], [1, 1, 1], [1, 1, 0]], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.fill(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
