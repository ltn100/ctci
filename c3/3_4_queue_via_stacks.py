import pytest


class QueueViaStacks:
    """
    A queue data structure that is composed of two stacks.
    """
    def __init__(self):
        self.fstack = []  # forward stack
        self.rstack = []  # reverse stack

    def push(self, val):
        self._move_to_forward()
        self.fstack.append(val)

    def pop(self):
        self._move_to_reverse()
        return self.rstack.pop()

    def peek(self):
        self._move_to_reverse()
        return self.rstack[-1]

    def _move_to_reverse(self):
        while self.fstack:
            self.rstack.append(self.fstack.pop())

    def _move_to_forward(self):
        while self.rstack:
            self.fstack.append(self.rstack.pop())


def test_queueviastacks():
    queue = QueueViaStacks()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    queue.push(6)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.pop() == 2
    queue.push(7)
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 5
    assert queue.peek() == 6
    assert queue.peek() == 6
    assert queue.pop() == 6
    assert queue.pop() == 7
    with pytest.raises(IndexError):
        queue.pop()


if __name__ == '__main__':
    pytest.main(args=[__file__])
