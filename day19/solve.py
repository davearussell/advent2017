#! /usr/bin/python3
import sys


def parse_input(path):
    lines = open(path).read().split('\n')
    grid = {}
    start = None
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if not cell.isspace():
                grid[(x, y)] = cell
                if start is None:
                    start = (x, y)
    return grid, start, (0, 1)


def main(input_file):
    grid, (x, y), (dx, dy) = parse_input(input_file)
    order = [grid[(x, y)]]

    while True:
        for (try_dx, try_dy) in [(dx, dy), (dy, dx), (-dy, -dx)]:
            cell = grid.get((x + try_dx, y + try_dy))
            if cell:
                dx, dy = try_dx, try_dy
                x, y = x + dx, y + dy
                order.append(cell)
                break
        else:
            break

    print("Part 1:", ''.join(x for x in order if x.isalpha()))
    print("Part 2:", len(order))


if __name__ == '__main__':
    main(sys.argv[1])
