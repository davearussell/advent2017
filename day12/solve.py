#! /usr/bin/python3
import sys


def parse_input(path):
    edges = {}
    for line in open(path):
        if not line.strip():
            continue
        spl = line.split(None, 2)
        node = int(spl[0])
        targets = [int(x) for x in spl[2].split(',')]
        for target in targets:
            edges.setdefault(node, set()).add(target)
            edges.setdefault(target, set()).add(node)
    return edges


def explore(edges, start):
    visited = set()
    frontier = {start}
    while frontier:
        visited |= frontier
        new_frontier = set()
        for node in frontier:
            new_frontier |= edges[node]
        frontier = new_frontier - visited
    return visited


def find_groups(edges):
    groups = []
    while edges:
        node = list(edges.keys())[0]
        group = explore(edges, node)
        groups.append(group)
        for node in groups[-1]:
            del edges[node]
    return groups


def main(input_file):
    edges = parse_input(input_file)
    print("Part 1:", len(explore(edges, 0)))
    print("Part 1:", len(find_groups(edges)))


if __name__ == '__main__':
    main(sys.argv[1])
