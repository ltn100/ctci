import pytest


class SetOfStacks:
    """
    A stack data structure that is composed of a set of stacks, where each stack
    cannot grow larger than a given size.
    """
    def __init__(self, max_len=128):
        self.stacks = []
        self.max_len = max_len

    def push(self, val):
        if len(self.stacks) == 0:
            self.stacks.append([])

        if len(self.stacks[-1]) >= self.max_len:
            self.stacks.append([])

        self.stacks[-1].append(val)

    def pop(self):
        while True:
            end_stack = self.stacks[-1]
            try:
                val = end_stack.pop()
                return val
            except IndexError:
                self.stacks.pop()

    def peek(self):
        while True:
            end_stack = self.stacks[-1]
            try:
                val = end_stack[-1]
                return val  
            except IndexError:
                self.stacks.pop()

    def popAt(self, index):
        return self.stacks[index].pop()


def test_setofstacks():
    stack = SetOfStacks(3)
    with pytest.raises(IndexError):
        stack.pop()
    stack.push(10)
    assert stack.peek() == 10
    stack.push(5)
    stack.push(1)
    stack.push(30)
    assert stack.pop() == 30
    assert stack.pop() == 1
    assert stack.pop() == 5
    assert stack.pop() == 10
    with pytest.raises(IndexError):
        stack.pop()


def test_popat():
    stack = SetOfStacks(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    assert stack.popAt(0) == 3
    assert stack.popAt(0) == 2
    assert stack.popAt(0) == 1
    assert stack.popAt(1) == 6
    assert stack.popAt(2) == 9

    assert stack.pop() == 8
    assert stack.pop() == 7
    assert stack.pop() == 5
    assert stack.pop() == 4
    with pytest.raises(IndexError):
        stack.pop()


if __name__ == '__main__':
    pytest.main(args=[__file__])
