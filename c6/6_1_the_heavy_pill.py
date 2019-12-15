import pytest


class Pill:
    def __init__(self, weight):
        self.weight = weight

    def __radd__(self, other):
        """
        To support the sum() function
        """
        return other + self.weight


class Bottle:
    def __init__(self, pills=0, heavy=False):
        if heavy:
            self.pills = [Pill(1.1) for _ in range(pills)]
        else:
            self.pills = [Pill(1.0) for _ in range(pills)]

    def take_pill(self):
        return self.pills.pop()

    def put_pill(self, pill):
        return self.pills.append(pill)

    def empty(self):
        return len(self.pills) == 0


class Solution:
    def get_heavy_index(self, bottles):
        """
        Given a number of pill bottles, find the one with the heavy pills
        while only using the scales once.

        :param bottles: List of pill bottles
        :return: The index of the heavy pill bottle
        """
        b = Bottle()  # empty bottle
        for i in range(len(bottles)):
            for _ in range(i+1):
                b.put_pill(bottles[i].take_pill())

        total_weight = self.weigh([b])  # only called once
        expected_weight = float((len(bottles)+1)*len(bottles)/2.0)
        diff = total_weight - expected_weight
        return diff // 0.1

    def weigh(self, bottles):
        weight = 0
        for bottle in bottles:
            weight += sum(bottle.pills)
        return weight


def test_solution():
    s = Solution()

    heavy = [False]*20
    heavy[15] = True
    bottles = [Bottle(100, h) for h in heavy]

    assert s.get_heavy_index(bottles) == 15

    heavy = [False]*100
    heavy[74] = True
    bottles = [Bottle(100, h) for h in heavy]

    assert s.get_heavy_index(bottles) == 74


if __name__ == '__main__':
    pytest.main(args=[__file__])
