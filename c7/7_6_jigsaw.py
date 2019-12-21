import pytest
from contextlib import ExitStack as does_not_raise


class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fits_with(self, other):
        if self.x == other.x:
            return abs(self.y - other.y) == 1
        elif self.y == other.y:
            return abs(self.x - other.x) == 1
        else:
            return False


class Jigsaw:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.unplaced_pieces = set()
        self.placed_pieces = [[None]*self.width for _ in range(self.height)]
        for h in range(self.height):
            for w in range(self.width):
                self.unplaced_pieces.add(Piece(w, h))

    def get_unplaced_pieces(self):
        return self.unplaced_pieces

    def place(self, piece, x, y):
        if self.placed_pieces[y][x] is not None:
            return False
        self.unplaced_pieces.remove(piece)
        self.placed_pieces[y][x] = piece

    def is_solved(self):
        for h in range(self.height):
            for w in range(self.width):
                if not self.placed_pieces[h][w] or self.placed_pieces[h][w].x != w or self.placed_pieces[h][w].y != h:
                    return False
        return True


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
