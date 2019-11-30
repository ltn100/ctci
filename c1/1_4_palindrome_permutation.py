import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def palindrome_permutation(self, s):
        """
        Check if string is a permutation of a palindrome. Ignore case and non-letter characters.

        There can be, at most, one odd count of a letter. Keep track of odd/even counts using a bit array.

        :param s: input string
        :return: True if s is permutation of a palindrome
        """
        bitarray = 0  # create empty bit vector
        for c in s:
            char_num = self.get_letter_num(c)
            if char_num is not None:
                bitarray ^= 1 << char_num  # toggle bit

        non_even_chars = 0
        while bitarray > 0:
            non_even_chars += bitarray & 1
            if non_even_chars > 1:
                return False
            bitarray >>= 1
        return True

    def get_letter_num(self, char):
        """
        Get the letter num (ord) of the lowercase letter. If a non-letter character
        is given, None is returned

        :param char: character
        :return: ord of lowercase char or None
        """
        char = char.lower()
        if char < 'a' or char > 'z':
            return None
        else:
            return ord(char)


testdata = [
    (("Tact Coa",), True, does_not_raise()),  # tacocat
    (("raCe 123 car#&!",), True, does_not_raise()),  # racecar
    (("a",), True, does_not_raise()),
    (("aa",), True, does_not_raise()),
    (("ab",), False, does_not_raise()),
    (("a2134124 !!£$23523532b",), False, does_not_raise()),
    (("dactCoa",), False, does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.palindrome_permutation(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
