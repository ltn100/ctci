import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    MOVES = {
        'D': [1, 0],
        'R': [0, 1]
    }

    def get_path(self, r, c, blocked):
        """
        Find path from top left of grid to bottom right by only moving
        right or down.

        :param r: number of rows in grid
        :param c: number of columns in grid
        :param blocked: list of blocked coordinates (r, c)
        :return: List of moves, as a string of "R" and "D" chars.
        """
        # Create grid
        grid = [[0]*c for _ in range(r)]
        for br, bc in blocked:
            grid[br][bc] = 1

        return self.get_path_helper(grid, 0, 0, "", set())

    def get_path_helper(self, grid, r, c, current_moves, visited):
        if r == len(grid)-1 and c == len(grid[r])-1:
            return current_moves

        if (r, c) in visited:
            return None
        visited.add((r, c))

        if grid[r][c] == 1:
            # Blocked
            return None

        for nr, nc, dir in self.get_neighbours(grid, r, c):
            moves = self.get_path_helper(grid, nr, nc, current_moves+dir, visited)
            if moves is not None:
                return moves

        return None

    def get_neighbours(self, grid, r, c):
        neighbours = []
        for dir, (nr, nc) in self.MOVES.items():
            if r + nr < len(grid) and c + nc < len(grid[r+nr]):
                neighbours.append((r+nr, c+nc, dir))
        return neighbours


testdata = [
    ((2, 2, []), "DR", does_not_raise()),
    ((2, 2, [(1, 0)]), "RD", does_not_raise()),
    ((3, 3, []), "DDRR", does_not_raise()),
    ((3, 3, [(2, 1)]), "DRRD", does_not_raise()),
    ((3, 3, [(2, 1), (1, 1)]), "RRDD", does_not_raise()),
    ((3, 3, [(2, 1), (1, 1), (0, 1)]), None, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_path(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
