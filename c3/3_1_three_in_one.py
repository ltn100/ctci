import pytest


class MultiStack:
    """
    A data structure that implements multiple stacks using a single array.
    """
    def __init__(self, num_stacks=3, init_size=256):
        self.num_stacks = num_stacks
        self.array = [None]*(init_size*num_stacks)
        self.stack_len = [0]*num_stacks

    def _get_offset(self, stack, increment=0):
        if stack >= self.num_stacks:
            raise IndexError("stack number to large")

        if self.stack_len[stack] + increment < 1:
            raise IndexError("stack is empty")

        lower = (len(self.array) // self.num_stacks) * stack
        upper = (len(self.array) // self.num_stacks) * (stack+1) - 1
        offset = lower + self.stack_len[stack] + increment - 1
        if offset > upper:
            raise IndexError("stack exceeds range")

        return offset

    def push(self, val, stack=0):
        offset = self._get_offset(stack, 1)
        self.array[offset] = val
        self.stack_len[stack] += 1

    def pop(self, stack=0):
        offset = self._get_offset(stack)
        val, self.array[offset] = self.array[offset], None
        self.stack_len[stack] -= 1
        return val

    def peek(self, stack=0):
        offset = self._get_offset(stack)
        return self.array[offset]

    def len(self, stack=0):
        return self.stack_len[stack]


def test_multistack():
    stack = MultiStack(3)
    stack.push(10, 0)
    assert stack.len(0) == 1
    stack.push(20, 1)
    assert stack.len(1) == 1
    stack.push(30, 2)
    assert stack.len(2) == 1
    with pytest.raises(IndexError):
        stack.push(40, 3)
    assert stack.peek(0) == 10
    assert stack.pop(0) == 10
    assert stack.len(0) == 0
    assert stack.len(1) == 1
    assert stack.len(2) == 1
    assert stack.pop(1) == 20
    assert stack.pop(2) == 30
    with pytest.raises(IndexError):
        stack.pop(3)
    with pytest.raises(IndexError):
        stack.pop(0)


if __name__ == '__main__':
    pytest.main(args=[__file__])
