#! /usr/bin/python3
import sys
import numba


def part1(n, steps):
    ring = [0] * (n + 1)
    current = 0
    for i in range(1, n + 1):
        _current = current
        for _ in range(steps):
            current = ring[current]
        ring[i] = ring[current]
        ring[current] = i
        current = i
    return ring[current]


@numba.njit(cache=True)
def part2(n, steps):
    result  = current = 0
    for i in range(1, n + 1):
        insert_after = (current + steps) % i
        current = insert_after + 1
        if not insert_after:
            result = i
    return result


def main(input_file):
    steps = int(open(input_file).read())
    print("Part 1:", part1(2017, steps))
    print("Part 2:", part2(50000000, steps))


if __name__ == '__main__':
    main(sys.argv[1])
