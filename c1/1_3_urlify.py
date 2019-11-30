import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    ENC_SPACE = bytearray(b'%20')

    def urlify(self, url, length):
        """
        Replace all spaces with '%20'

        Count spaces. Iterate from end of string replacing characters.

        :param url: bytearray to encode
        :param length: length of string
        :return: mutated bytearray
        """
        # Count spaces
        spaces = 0
        for c in range(length):
            if url[c] == ord(' '):
                spaces += 1

        # Check bounds
        output_end = length + (len(self.ENC_SPACE)-1)*spaces
        if len(url) < output_end:
            raise IndexError("encoded string would overrun array bounds")

        # Iterate backwards replacing spaces
        input_end = length
        while input_end > 0:
            if url[input_end-1] == ord(' '):
                url[output_end-len(self.ENC_SPACE):output_end] = self.ENC_SPACE
                output_end -= len(self.ENC_SPACE)
            else:
                url[output_end-1] = url[input_end-1]
                output_end -= 1
            input_end -= 1

        return url


testdata = [
    ((bytearray(b"Mr John Smith    "), 13), bytearray(b"Mr%20John%20Smith"), does_not_raise()),
    ((bytearray(b"noreplacements"), 14), bytearray(b"noreplacements"), does_not_raise()),
    ((bytearray(b"inputoverflow"), 5), bytearray(b"inputoverflow"), does_not_raise()),
    ((bytearray(b"     "), 1), bytearray(b"%20  "), does_not_raise()),
    ((bytearray(b"out of bounds"), 13), None, pytest.raises(IndexError)),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.urlify(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
