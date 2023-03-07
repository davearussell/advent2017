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


def hash(input_bytes):
    data = list(range(256))
    lengths = list(input_bytes) + [17, 31, 73, 47, 23]
    pos = skip = 0
    for _ in range(64):
        data, pos, skip = hash_round(data, lengths, pos, skip)
    xor = 0
    hashed = 0
    for i, value in enumerate(data):
        xor ^= value
        if i & 0xf == 0xf:
            hashed = (hashed << 8) | xor
            xor = 0
    return hashed


def make_grid(key):
    grid = set()
    for i in range(128):
        value = hash(b'%s-%d' % (key, i))
        for j in range(128):
            if value & (1 << j):
                grid.add((i, j))
    return grid


def explore(grid, start):
    visited = set()
    frontier = {start}
    while frontier:
        visited |= frontier
        new_frontier = set()
        for x, y in frontier:
            neighbours = {(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)}
            new_frontier |= neighbours
        frontier = (new_frontier - visited) & grid
    return visited


def find_groups(grid):
    groups = []
    while grid:
        pos = grid.pop()
        group = explore(grid, pos)
        groups.append(group)
        grid -= group
    return groups


def main(input_file):
    key = open(input_file, 'rb').read().strip()
    grid = make_grid(key)
    print("Part 1:", len(grid))
    groups = find_groups(grid)
    print("Part 2:", len(groups))


if __name__ == '__main__':
    main(sys.argv[1])
