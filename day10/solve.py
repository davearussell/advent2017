#! /usr/bin/python3
import sys


def hash_round(data, lengths, pos, skip):
    # In order to avoid the need to handle wrapping, we rotate data before
    # each operation so that the current element is at the start of the list
    data = data[pos:] + data[:pos]
    for length in lengths:
        data = data[:length][::-1] + data[length:]
        rotate_by = (skip + length) % len(data)
        data = data[rotate_by:] + data[:rotate_by]
        pos = (pos + rotate_by) % len(data)
        skip += 1
    data = data[-pos:] + data[:-pos] # reverses the rotations described above
    return data, pos, skip


def part1(input_bytes, data):
    lengths = [int(x) for x in input_bytes.split(b',')]
    data, _, _ = hash_round(data, lengths, 0, 0)
    return data[0] * data[1]


def part2(input_bytes, data):
    lengths = list(input_bytes) + [17, 31, 73, 47, 23]
    pos = skip = 0
    for _ in range(64):
        data, pos, skip = hash_round(data, lengths, pos, skip)
    xor = 0
    hashed = ''
    for i, value in enumerate(data):
        xor ^= value
        if i & 0xf == 0xf:
            hashed += '%02x' % xor
            xor = 0
    return hashed


def main(input_file):
    input_bytes = open(input_file, 'rb').read().strip()
    data = list(range(256))
    print("Part 1:", part1(input_bytes, data))
    print("Part 2:", part2(input_bytes, data))


if __name__ == '__main__':
    main(sys.argv[1])
