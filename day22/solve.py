#! /usr/bin/python3
import sys

RIGHT = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
}
LEFT = {v: k for (k, v) in RIGHT.items()}


C, W, I, F = range(4)
def parse_input(path):
    cells = open(path).read().strip().split('\n')
    h = len(cells)
    w = len(cells[0])
    assert h & w & 1
    grid = {}
    for y, row in enumerate(cells):
        for x, cell in enumerate(row):
            if cell == '#':
                grid[(x, y)] = I
    return grid, (w // 2, h // 2), (0, -1)


def tick1(grid, pos, facing):
    state = grid.get(pos, C)
    if state == I:
        facing = RIGHT[facing]
        grid[pos] = C
    else:
        facing = LEFT[facing]
        grid[pos] = I
    pos = (pos[0] + facing[0], pos[1] + facing[1])
    return pos, facing, state == C


def tick2(grid, pos, facing):
    state = grid.get(pos, C)
    if state == C:
        facing = LEFT[facing]
        grid[pos] = W
    elif state == W:
        grid[pos] = I
    elif state == I:
        facing = RIGHT[facing]
        grid[pos] = F
    elif state == F:
        facing = RIGHT[RIGHT[facing]]
        grid[pos] = C

    pos = (pos[0] + facing[0], pos[1] + facing[1])
    return pos, facing, state == W


def run_for(grid, pos, facing, ticker, n):
    infections = 0
    for i in range(n):
        pos, facing, infected = ticker(grid, pos, facing)
        infections += infected
    return infections


def main(input_file):
    grid, pos, facing = parse_input(input_file)
    print("Part 1:", run_for(grid, pos, facing, tick1, 10000))

    grid, pos, facing = parse_input(input_file)
    print("Part 2:", run_for(grid, pos, facing, tick2, 10000000))


if __name__ == '__main__':
    main(sys.argv[1])
