import pytest
from contextlib import ExitStack as does_not_raise
import threading
import time


class FizzBuzzThread(threading.Thread):
    LOCK = threading.Lock()
    NUM = 1
    RESULT = []

    def __init__(self, f3, f5, max, fout):
        super().__init__()
        self.f3 = f3
        self.f5 = f5
        self.max = max
        self.fout = fout

    def run(self):
        while True:
            time.sleep(0.01)
            with FizzBuzzThread.LOCK:
                if FizzBuzzThread.NUM > self.max:
                    return
                if self.f3(FizzBuzzThread.NUM) and self.f5(FizzBuzzThread.NUM):
                    FizzBuzzThread.RESULT.append(str(self.fout(FizzBuzzThread.NUM)))
                    FizzBuzzThread.NUM += 1


class Solution:
    def problem(self, n):
        """
        description

        :param arg:
        :return:
        """
        threads = [
            FizzBuzzThread(lambda x: x % 3 == 0, lambda x: x % 5 != 0, n, lambda _: "Fizz"),
            FizzBuzzThread(lambda x: x % 3 != 0, lambda x: x % 5 == 0, n, lambda _: "Buzz"),
            FizzBuzzThread(lambda x: x % 3 == 0, lambda x: x % 5 == 0, n, lambda _: "FizzBuzz"),
            FizzBuzzThread(lambda x: x % 3 != 0, lambda x: x % 5 != 0, n, lambda i: i)
        ]

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        return FizzBuzzThread.RESULT


testdata = [
    ((3,), ["1", "2", "Fizz"], does_not_raise()),
    ((16,), ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16"], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.problem(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
