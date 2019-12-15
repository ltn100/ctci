import pytest
from contextlib import ExitStack as does_not_raise


class Soda:
    def __init__(self, poison=False):
        self.poison = poison

    def __repr__(self):
        return "X" if self.poison else "O"

    def mix(self, other):
        self.poison = self.poison or other.poison


class PoisonTestStick:
    def __init__(self):
        self.result = None

    def test(self, soda):
        self.result = soda.poison

    def is_poisoned(self):
        return self.result


class Solution:
    def get_poison_index(self, sodas, test_sticks):
        """
        Given a number of sodas and test sticks determine the index of the
        one poisoned soda.

        :param sodas: List of sodas
        :return: Index of poisoned soda
        """
        test_sodas = [Soda() for _ in range(len(test_sticks))]
        for soda_i in range(len(sodas)):
            bit = 0
            i = soda_i
            while i:
                if i & 1:
                    test_sodas[bit].mix(sodas[soda_i])
                i >>= 1
                bit += 1

        for i in range(len(test_sticks)):
            test_sticks[i].test(test_sodas[i])

        # Wait for results

        index = 0
        for i in range(len(test_sticks)):
            index += 2**i if test_sticks[i].is_poisoned() else 0

        return index


def test_solution():
    s = Solution()

    poison = [False]*1000
    poison[576] = True
    bottles = [Soda(p) for p in poison]
    test_sticks = [PoisonTestStick() for _ in range(10)]

    assert s.get_poison_index(bottles, test_sticks) == 576


if __name__ == '__main__':
    pytest.main(args=[__file__])
