#! /usr/bin/python3
import sys

class Group:
    def __init__(self):
        self.children = []
        self.parent = None
        self.score = 1
        self.sum_score = 1

    def resolve(self):
        for child in self.children:
            if isinstance(child, Group):
                child.score = self.score + 1
                child.resolve()
        self.sum_score = self.score + sum(child.sum_score for child in self.children)
        self.garbage_count = sum(child.garbage_count for child in self.children)


class Garbage:
    def __init__(self):
        self.text = ''
        self.sum_score = 0
        self.parent = None

    @property
    def garbage_count(self):
        return len(self.text)


def parse_input(path):
    s = open(path).read().strip()
    assert s[0] == '{'
    root = Group()
    current = root
    ignore = False
    accept_child = True

    for char in s[1:]:
        if isinstance(current, Garbage):
            if ignore:
                ignore = False
            elif char == '>':
                current = current.parent
                accept_child = False
            elif char == '!':
                ignore = True
            else:
                current.text += char
        elif char == '}':
            current = current.parent
            accept_child = False
        elif char in '{<':
            assert accept_child
            child = Group() if char == '{' else Garbage()
            accept_child = True
            current.children.append(child)
            child.parent = current
            current = child
        elif char == ',':
            accept_child = True
    root.resolve()
    return root


def main(input_file):
    root = parse_input(input_file)
    print("Part 1:", root.sum_score)
    print("Part 2:", root.garbage_count)


if __name__ == '__main__':
    main(sys.argv[1])
