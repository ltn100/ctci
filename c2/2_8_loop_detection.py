import pytest
from contextlib import ExitStack as does_not_raise
from linkedlist import Node


class Solution:
    def get_loop_node(self, node):
        """
        Detect if a loop exists in a list, and if so, return the node at the start of the loop.

        Use fast/slow pointers. If they collide, there is a loop.

        The collision point will be exactly the same distance from the loop start point as the head of the
        head of the linked list is from the loop start point (mod the size of the loop). Therefore we start
        one pointer from the head of the list, and one from the collision point and iterate at the same speed
        until they collide. This new collision point will be the start of the loop.

        :param node: Head node
        :return: Node at the start of a loop, or None
        """
        p1 = node  # slow
        p2 = node  # fast

        # Iterate at slow/fast pace
        while True:
            if p1 is None or p2 is None or p2.next is None:
                # No loop
                return None

            p1 = p1.next
            p2 = p2.next.next

            if p1 is p2:
                # Loop detected
                break

        # Reset p2 to head of list and iterate both at same pace
        p2 = node
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next

        return p1

    def get_loop_node_id(self, node):
        """
        Helper function to avoid infinite loop in test case
        """
        loop_node = self.get_loop_node(node)
        return id(loop_node) if loop_node else None


loop_list = Node.from_array([1, 2, 3, 4, 5, 6])
loop_list.end().next = loop_list.next.next

testdata = [
    ((loop_list,), id(loop_list.next.next), does_not_raise()),
    ((Node.from_array([1, 2, 3, 4, 5, 6]),), None, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_loop_node_id(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
