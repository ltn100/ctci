import pytest
from contextlib import ExitStack as does_not_raise


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def __repr__(self):
        return str(self.val)


class Solution:
    def has_route(self, start, end):
        """
        Return True if there is a route from start to end.

        DFS graph traversal.

        :param start: Start node
        :param end: End node
        :return: True if nodes are connected
        """
        return self.has_route_helper(start, end, set())

    def has_route_helper(self, start, end, visited):
        if start is end:
            return True

        if start in visited:
            return False

        visited.add(start)

        for child in start.children:
            if self.has_route(child, end):
                return True

        return False


# 0      8
# |\     |
# 1 2    9
# |\ \
# 3 4 5
# |/  |
# 6   7
nodes = [Node(i) for i in range(10)]
nodes[0].children.append(nodes[1])
nodes[0].children.append(nodes[2])
nodes[1].children.append(nodes[3])
nodes[1].children.append(nodes[4])
nodes[2].children.append(nodes[5])
nodes[3].children.append(nodes[6])
nodes[4].children.append(nodes[6])
nodes[5].children.append(nodes[7])
nodes[8].children.append(nodes[9])

testdata = [
    ((nodes[0], nodes[1]), True, does_not_raise()),
    ((nodes[0], nodes[7]), True, does_not_raise()),
    ((nodes[0], nodes[6]), True, does_not_raise()),
    ((nodes[0], nodes[9]), False, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.has_route(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
