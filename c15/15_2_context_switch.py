import pytest
import os
import time


class Solution:
    TOKEN = b't'

    def __init__(self):
        self.pipein12, self.pipeout12 = os.pipe()  # pipe from p1 -> p2
        self.pipein21, self.pipeout21 = os.pipe()  # pipe from p2 -> p1
        self.pipein33, self.pipeout33 = os.pipe()  # pipe from p3 -> p3

    def run(self):
        if os.fork() == 0:
            self.p2()
            exit()
        else:
            runtime_with_ctx_switch = self.p1()
            runtime_without_ctx_switch = self.p3()
            return runtime_with_ctx_switch - runtime_without_ctx_switch

    def p1(self):
        start = time.time()
        os.write(self.pipeout12, self.TOKEN)  # context switch to p2
        _ = os.read(self.pipein21, len(self.TOKEN))  # context switch back to p1
        end = time.time()
        return (end - start) / 2

    def p2(self):
        _ = os.read(self.pipein12, len(self.TOKEN))
        os.write(self.pipeout21, self.TOKEN)

    def p3(self):
        start = time.time()
        os.write(self.pipeout33, self.TOKEN)
        _ = os.read(self.pipein33, len(self.TOKEN))
        os.write(self.pipeout33, self.TOKEN)
        _ = os.read(self.pipein33, len(self.TOKEN))
        end = time.time()
        return (end - start) / 2


def tst_solution():
    s = Solution()
    context_switch_ms = s.run()*1000
    assert 0.1 < context_switch_ms < 0.3


if __name__ == '__main__':
    #pytest.main(args=[__file__])
    tst_solution()  # pytest does not play nice with forks

