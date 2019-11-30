import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def compress_string(self, s):
        """
        Return a RLE string, if the string would compress.

        Generate a list of string characters and do one join() operation to
        avoid a large number of string concatenations (these are expensive, and
        pollute the string pool).

        :param s: String to attempt to compress
        :return: Compressed string if shorter than original, else original.
        """
        compressed = []
        current_char = ''
        char_count = 0
        total_len = 0

        for c in s:
            if c != current_char:
                if current_char:
                    compressed.append(current_char)
                    total_len += 1
                    compressed.append(str(char_count))
                    total_len += len(compressed[-1])
                    if total_len > len(s):
                        return s
                char_count = 0
                current_char = c

            char_count += 1

        compressed.append(current_char)
        total_len += 1
        compressed.append(str(char_count))
        total_len += len(compressed[-1])
        if total_len >= len(s):
            return s

        return "".join(compressed)


testdata = [
    (("aabcccccaaa",), "a2b1c5a3", does_not_raise()),
    (("a"*100,), "a100", does_not_raise()),
    (("a",), "a", does_not_raise()),
    (("abc",), "abc", does_not_raise()),
    (("aabccaaa",), "aabccaaa", does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.compress_string(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
