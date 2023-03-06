#! /usr/bin/python3
import sys


def divide(row):
    for n in sorted(row):
        for i in range(2, max(row) // n + 1):
            if n * i in row:
                return i


def main(input_file):
    table = [[int(x) for x in line.split()] for line in open(input_file)]
    print("Part 1:", sum(max(row) - min(row) for row in table))
    print("Part 2:", sum(map(divide, table)))


if __name__ == '__main__':
    main(sys.argv[1])
