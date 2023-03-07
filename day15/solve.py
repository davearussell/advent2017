#! /usr/bin/python3
import sys
import numba

FA = 16807
FB = 48271
MASK = (1 << 16) - 1
DIVISOR = (1 << 31) - 1

@numba.njit(cache=True)
def part1(a, b, n):
    count = 0
    for i in range(n):
        a = (a * FA) % DIVISOR
        b = (b * FB) % DIVISOR
        if (a & MASK) == (b & MASK):
            count += 1
    return count


@numba.njit(cache=True)
def part2(a, b, n):
    count = 0
    for i in range(n):
        a = (a * FA) % DIVISOR
        while a & 3:
            a = (a * FA) % DIVISOR
        b = (b * FB) % DIVISOR
        while b & 7:
            b = (b * FB) % DIVISOR
        if (a & MASK) == (b & MASK):
            count += 1
    return count


def main(input_file):
    a, b = [int(x) for x in open(input_file).read().split() if x.isdigit()]
    print("Part 1:", part1(a, b, 40000000))
    print("Part 2:", part2(a, b, 5000000))


if __name__ == '__main__':
    main(sys.argv[1])
