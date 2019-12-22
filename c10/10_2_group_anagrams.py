import pytest
from contextlib import ExitStack as does_not_raise
from collections import defaultdict


class Solution:
    def key_func(self, s):
        return "".join(sorted(s))

    def group_anagrams_sort(self, arr):
        """
        Given an array of strings, sort them so that anagrams are next to one another.

        :param arr: Array of strings
        :return:
        """
        arr = sorted(arr, key=self.key_func)
        return arr

    def group_anagrams_hashmap(self, arr):
        """
        Given an array of strings, sort them so that anagrams are next to one another.

        :param arr: Array of strings
        :return:
        """
        hashmap = defaultdict(list)
        for s in arr:
            hashmap["".join(sorted(s))].append(s)

        result = []
        for _, strings in hashmap.items():
            for s in strings:
                result.append(s)
        return result

testdata = [
    ((["car", "dog", "god", "rac", "dgo"],), ["car", "rac", "dog", "god", "dgo"], does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.group_anagrams_sort(*args) == res


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.group_anagrams_hashmap(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
