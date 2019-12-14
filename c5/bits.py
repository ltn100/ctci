def b2i(s, base=2):
    return int(s, base=base)


def b2bytearray(s):
    if len(s) % 8 != 0:
        raise ValueError("String must be a whole number of bytes")

    num_bytes = len(s)//8
    ba = bytearray(num_bytes)
    for i in range(num_bytes):
        ba[i] = int(s[i*8:(i+1)*8][::-1], base=2)  # reverse string for each byte to make it visually correct
    return ba
