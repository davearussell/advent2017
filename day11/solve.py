#! /usr/bin/python3
import sys

OFFSETS = {
    'n': (0, -2),
    'ne': (1, -1),
    'nw': (-1, -1),
    's': (0, 2),
    'se': (1, 1),
    'sw': (-1, 1),
}


def distance(x, y):
    steps = abs(x)
    if abs(y) > steps:
        steps += (abs(y) - steps) // 2
    return steps


def main(input_file):
    moves = open(input_file).read().strip().split(',')
    x = y = max_steps = 0
    for move in moves:
        dx, dy = OFFSETS[move]
        x, y = x + dx, y + dy
        steps = distance(x, y)
        max_steps = max(max_steps, steps)
    print("Part 1:", steps)
    print("Part 2:", max_steps)


if __name__ == '__main__':
    main(sys.argv[1])
