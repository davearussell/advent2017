#! /usr/bin/python3
import math
import sys


def get_pos(n):
    if n == 1:
        return (0, 0)
    region = int(math.ceil(n ** .5)) // 2
    region_start = (region * 2 - 1) ** 2 + 1
    region_len = region * 8
    offset = n - region_start
    quadrant, qoff = divmod(offset, region_len // 4)
    if quadrant == 0:
        x, y = region, region - qoff - 1
    elif quadrant == 1:
        x, y = region - qoff - 1, -region
    elif quadrant == 2:
        x, y = -region, -(region - qoff - 1)
    else:
        x, y = -(region - qoff - 1), region
    return x, y


def main(text):
    input_value = int(text)
    print("Part 1:", sum(map(abs, get_pos(input_value))))

    grid = {get_pos(1): 1}
    for i in range(2, input_value):
        x, y = get_pos(i)
        neighbours = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                      (x - 1, y), (x + 1, y),
                      (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
        value = sum(grid.get(n, 0) for n in neighbours)
        if value > input_value:
            print("Part 2:", value)
            break
        grid[(x, y)] = value

if __name__ == '__main__':
    main(sys.argv[1])
