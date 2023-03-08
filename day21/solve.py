#! /usr/bin/python3
import sys

import numpy


def to_array(text):
    grid = [['.#'.index(cell) for cell in row] for row in text.split('/')]
    return numpy.array(grid, dtype=numpy.uint8)


def parse_input(path):
    rules = {}
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        lhs, rhs = line.split(' => ')
        lhs = to_array(lhs)
        rhs = to_array(rhs)
        for permutation in [
                lhs,
                numpy.flipud(lhs),
                numpy.fliplr(lhs),
                numpy.flipud(numpy.rot90(lhs)),
                numpy.fliplr(numpy.rot90(lhs)),
                numpy.rot90(lhs),
                numpy.rot90(numpy.rot90(lhs)),
                numpy.rot90(numpy.rot90(numpy.rot90(lhs))),
        ]:
            rules[permutation.tobytes()] = rhs
    return rules


def iterate(grid, rules):
    size = len(grid)
    cell_size = 2 if size % 2 == 0 else 3
    new_cell_size = cell_size + 1
    new_size = size * new_cell_size // cell_size
    new_grid = numpy.zeros([new_size, new_size], dtype=numpy.uint8)

    for i in range(size // cell_size):
        for j in range(size // cell_size):
            i0, i1 = i * cell_size, (i + 1) * cell_size
            j0, j1 = j * cell_size, (j + 1) * cell_size
            x0, x1 = i * new_cell_size, (i + 1) * new_cell_size
            y0, y1 = j * new_cell_size, (j + 1) * new_cell_size
            k = grid[i0 : i1, j0 : j1].tobytes()
            new_grid[x0 : x1, y0 : y1] = rules[k]
    return new_grid


def main(input_file):
    rules = parse_input(input_file)
    grid = to_array(".#./..#/###")
    for i in range(18):
        grid = iterate(grid, rules)
        print("After %d steps, %d pixels are on" % (i + 1, numpy.count_nonzero(grid)))


if __name__ == '__main__':
    main(sys.argv[1])
