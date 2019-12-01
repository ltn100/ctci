import pytest
from contextlib import ExitStack as does_not_raise
from linkedlist import Node


class Solution:
    def get_intersection(self, l1, l2):
        """
        Get intersection of two lists (first node common to both lists). If there is no intersection, return None.

        Iterate through each list and see if the tail nodes are the same. At the same time get the lengths.

        Chop off the difference in lengths of the longest list. Then iterate through each list at the same speed
        until the nodes are the same (by reference).

        :param l1: List 1
        :param l2: List 2
        :return: Intersecting node, or None
        """
        if l1 is None or l2 is None:
            return None

        # Get lengths and tail nodes
        tail1, length1 = l1, 1
        while tail1.next is not None:
            tail1 = tail1.next
            length1 += 1

        tail2, length2 = l2, 1
        while tail2.next is not None:
            tail2 = tail2.next
            length2 += 1

        if tail1 is not tail2:
            # References to not match; no intersection
            return None

        # Move pointers to match lengths
        while length1 < length2:
            l2 = l2.next
            length2 -= 1

        while length1 > length2:
            l1 = l1.next
            length1 -= 1

        # Iterate until pointers intersect
        while l1.next is not None:
            if l1 is l2:
                return l1
            l1 = l1.next
            l2 = l2.next

        # Should never get here
        raise RuntimeError("l1 {} and l2 {} did something strange".format(l1, l2))


intersect = Node.from_array([10, 20, 30, 40])
list1 = Node.from_array([1, 2, 3, 4])
list1.end().next = intersect
list2 = Node.from_array([2, 4, 6, 8])
list2.end().next = intersect

testdata = [
    ((list1, list2), intersect, does_not_raise()),
    ((list1, list1), list1, does_not_raise()),
    ((list1, Node.from_array([42])), None, does_not_raise()),
    ((Node.from_array([1]), Node.from_array([1])), None, does_not_raise()),
    ((Node.from_array([]), Node.from_array([])), None, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.get_intersection(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
