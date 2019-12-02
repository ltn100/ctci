import pytest


class MinStack:
    """
    A stack data structure that also supports getting the min value in O(1) time.
    """
    def __init__(self):
        self.stack = []

    def push(self, val):
        new_min = min(self.stack[-1][1], val) if self.stack else val
        self.stack.append((val, new_min))

    def pop(self):
        return self.stack.pop()[0]

    def peek(self):
        return self.stack[-1][0]

    def min(self):
        return self.stack[-1][1]


def test_stackmin():
    stack = MinStack()
    with pytest.raises(IndexError):
        stack.min()
    stack.push(10)
    assert stack.peek() == 10
    assert stack.min() == 10
    stack.push(5)
    stack.push(1)
    stack.push(30)
    assert stack.min() == 1
    assert stack.pop() == 30
    assert stack.min() == 1
    assert stack.pop() == 1
    assert stack.min() == 5
    assert stack.pop() == 5
    assert stack.min() == 10
    assert stack.pop() == 10
    with pytest.raises(IndexError):
        stack.min()


if __name__ == '__main__':
    pytest.main(args=[__file__])
