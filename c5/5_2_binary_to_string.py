import pytest
from contextlib import ExitStack as does_not_raise


class Solution:
    def binary_to_string(self, f):
        """
        Given a decimal floating point number, return its binary representation as a string

        Raises a ValueError exception if the string cannot be fully represented with 32 chars

        :param f: Floating point number
        :return: String representation
        """
        # Create string list, for efficient string building
        sl = ["0", "."]

        while f > 0.0 and len(sl) < 32:
            # Multiply by 2 and see if the number is > 1
            f *= 2
            # Add that to the binary representation
            sl.append(str(int(f // 1)))
            # Remove any leading 1
            f -= (f // 1)

        if f == 0.0:
            return "".join(sl)
        else:
            raise ValueError("Cannot represent num in 32 chars")


testdata = [
    ((0.5,), "0.1", does_not_raise()),
    ((0.890625,), "0.111001", does_not_raise()),
    ((0.1,), None, pytest.raises(ValueError)),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.binary_to_string(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
