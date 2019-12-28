import pytest
from contextlib import ExitStack as does_not_raise
import threading
import time
import random


class Chopstick:
    def __init__(self, i):
        self.lock = threading.Lock()
        self.index = i

    def acquire(self):
        self.lock.acquire()

    def release(self):
        self.lock.release()


class Philosopher:
    def __init__(self, left_chopstick, right_chopstick):
        if left_chopstick.index > right_chopstick.index:
            self.higher = left_chopstick
            self.lower = right_chopstick
        else:
            self.lower = left_chopstick
            self.higher = right_chopstick

        # This results in the deadlock, because there is a cycle:
        #self.left = left_chopstick
        #self.right = right_chopstick

    def eat(self):
        time.sleep(random.random()*0.1)
        self.lower.acquire()
        time.sleep(random.random()*0.1)
        self.higher.acquire()
        # Now eat :-)
        time.sleep(random.random()*0.1)
        self.higher.release()
        time.sleep(random.random()*0.1)
        self.lower.release()


class Solution:
    def problem(self, n):
        """
        Given a number of philosophers around a round table, with one chopstick on the left and
        one chopstick on the right, implement an algorithm so that everyone can eat.

        :param arg:
        :return:
        """
        cs = [Chopstick(i) for i in range(n)]
        ps = []
        for i in range(n-1):
            ps.append(Philosopher(cs[i], cs[i+1]))
        ps.append(Philosopher(cs[n-1], cs[0]))

        threads = []
        for i in range(n):
            t = threading.Thread(target=ps[i].eat)
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()


testdata = [
    ((5,), None, does_not_raise()),
    ((2,), None, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.problem(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
