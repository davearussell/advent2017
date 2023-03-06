#! /usr/bin/python3
import re
import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.weight = None
        self.children = []
        self.parent = None

    @property
    def total(self):
        return self.weight + sum(child.total for child in self.children)


def parse_input(path):
    pat = re.compile(r"(\S+) [(](\d+)[)](?: .. (.+))?")
    nodes = {}
    for line in open(path):
        x = pat.match(line)
        name, weight, children = x.groups()
        node = nodes.setdefault(name, Node(name))
        node.weight = int(weight)
        if children:
            for child_name in children.split(', '):
                child_node = nodes.setdefault(child_name, Node(child_name))
                child_node.parent = node
                node.children.append(child_node)
    roots = [node for node in nodes.values() if not node.parent]
    assert len(roots) == 1
    return roots[0]


def find_mismatch(node, target_weight):
    if not node.children:
        return target_weight
    if len({child.total for child in node.children}) == 1:
       return target_weight - node.children[0].total * len(node.children)
    child_target = (target_weight - node.weight) // len(node.children)
    if node.total < target_weight:
        bad_child = min(node.children, key=lambda c:c.total)
    else:
        bad_child = max(node.children, key=lambda c:c.total)
    return find_mismatch(bad_child, child_target)


def main(input_file):
    root = parse_input(input_file)
    print("Part 1:", root.name)
    assert len(root.children) > 2
    weights = [child.total for child in root.children]
    target_child_weight = max(set(weights), key=weights.count)
    target_weight = root.weight + target_child_weight * len(root.children)
    print("Part 2:", find_mismatch(root, target_weight))


if __name__ == '__main__':
    main(sys.argv[1])
