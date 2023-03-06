#! /usr/bin/python3
import sys


def redistribute(values):
    m = max(values)
    i = values.index(m)
    values[i] = 0
    n, r = divmod(m, len(values))
    for j in range(len(values)):
        values[j] += n
        if 1 <= ((j - i) % len(values)) <= r:
            values[j] += 1


def main(input_file):
    values = [int(x) for x in open(input_file).read().split()]
    seen = {}
    while True:
        t = tuple(values)
        if t in seen:
            print("Part 1:", len(seen))
            print("Part 2:", len(seen) - seen[t])
            break
        seen[t] = len(seen)
        redistribute(values)


if __name__ == '__main__':
    main(sys.argv[1])
