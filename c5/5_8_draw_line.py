import pytest
from contextlib import ExitStack as does_not_raise
from bits import b2bytearray

class Solution:
    def draw_line(self, screen, w, x1, x2, y):
        """
        Draw a horizontal line on a screen.

        A screen represented by bits in a byte array has width w bits.
        Draw a line from (x1, y) to (x2, y)

        :param screen: The screen, as a bytearray
        :param w: The width of the screen in bits (an integer divisible by 8)
        :param x1: The starting x coord
        :param x2: The ending x coord (exclusive)
        :param y: The y coord
        :return: The mutated screen buffer
        """
        start_bit = y*w + x1
        end_bit = y*w + x2

        start_byte = start_bit // 8
        end_byte = end_bit // 8
        start_offset = start_bit % 8
        end_offset = end_bit % 8

        if start_byte == end_byte:
            byte = 2**(end_offset-start_offset)-1
            byte <<= start_offset
            screen[start_byte] = byte
        else:
            # Start byte
            byte = 2**(8-start_offset)-1
            byte <<= start_offset
            screen[start_byte] = byte

            for mid_byte in range(start_byte+1, end_byte):
                screen[mid_byte] = 0xff

            # End byte
            if end_offset > 0:
                byte = 2**end_offset-1
                screen[end_byte] = byte

        print(screen)
        return screen


testdata = [
    ((bytearray(16), 4*8, 3, 7, 2),  b2bytearray("00000000000000000000000000000000"+"00000000000000000000000000000000"+"00011110000000000000000000000000"+"00000000000000000000000000000000"), does_not_raise()),
    ((bytearray(16), 4*8, 3, 22, 2), b2bytearray("00000000000000000000000000000000"+"00000000000000000000000000000000"+"00011111111111111111110000000000"+"00000000000000000000000000000000"), does_not_raise()),
    ((bytearray(16), 4*8, 3, 12, 2), b2bytearray("00000000000000000000000000000000"+"00000000000000000000000000000000"+"00011111111100000000000000000000"+"00000000000000000000000000000000"), does_not_raise()),
    ((bytearray(16), 4*8, (4*8)-1, 4*8, 3), b2bytearray("00000000000000000000000000000000"+"00000000000000000000000000000000"+"00000000000000000000000000000000"+"00000000000000000000000000000001"), does_not_raise()),
]


@pytest.mark.parametrize("args, res, expectation", testdata)
def test_solution(args, res, expectation):
    with expectation:
        s = Solution()
        assert s.draw_line(*args) == res


if __name__ == '__main__':
    pytest.main(args=[__file__])
