import pytest
from contextlib import ExitStack as does_not_raise


class Node:
    def __init__(self):
        self.count = 0
        self.children = {}

    def add_word(self, word):
        if not word:
            self.count += 1
            return

        if word[0] not in self.children:
            self.children[word[0]] = Node()

        self.children[word[0]].add_word(word[1:])

    def get_count(self, word):
        if not word:
            return self.count

        if word[0] not in self.children:
            return 0

        return self.children[word[0]].get_count(word[1:])


class Solution:
    def __init__(self, words):
        self.trie = Node()
        for word in words.split():
            self.trie.add_word(word)

    def get_frequency(self, word):
        """
        description

        :param arg:
        :return:
        """
        return self.trie.get_count(word)


testdata = [
    (("dog",), 2, does_not_raise()),
    (("doggy",), 1, does_not_raise()),
    (("car",), 1, does_not_raise()),
]

words = "dog cat rabbit mouse dog door doggy car caravan"


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution(words)
        assert s.get_frequency(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
