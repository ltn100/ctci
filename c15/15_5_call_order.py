import pytest
from contextlib import ExitStack as does_not_raise
import threading
import time
import random


class Foo:
    def __init__(self):
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)
        self.result = []
        self.result_lock = threading.Lock()

    def add_result(self, result):
        self.result_lock.acquire()
        self.result.append(result)
        self.result_lock.release()

    def first(self):
        time.sleep(random.random()*0.1)  # inject some randomness
        self.add_result(1)
        self.s1.release()

    def second(self):
        time.sleep(random.random()*0.1)
        self.s1.acquire()
        self.add_result(2)
        self.s1.release()
        self.s2.release()

    def third(self):
        time.sleep(random.random()*0.1)
        self.s2.acquire()
        self.add_result(3)
        self.s2.release()


class Solution:
    def problem(self, arg):
        """
        Ensure that the members of Foo are always called in the correct order.
        """
        foo = Foo()

        t1 = threading.Thread(target=foo.first)
        t2 = threading.Thread(target=foo.second)
        t3 = threading.Thread(target=foo.third)

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

        return foo.result


testdata = [
    (("arg",), [1, 2, 3], does_not_raise()),
    (("arg",), [1, 2, 3], does_not_raise()),
    (("arg",), [1, 2, 3], does_not_raise()),
    (("arg",), [1, 2, 3], does_not_raise()),
    (("arg",), [1, 2, 3], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.problem(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
