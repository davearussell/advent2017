#! /usr/bin/python3
import sys


def main(input_file):
    value = open(input_file).read().strip()
    def scorer(offset):
        def score(i):
            if value[i] == value[(i + offset) % len(value)]:
                return int(value[i])
            return 0
        return score
    print("Part 1:", sum(map(scorer(1), range(len(value)))))
    print("Part 2:", sum(map(scorer(len(value) // 2), range(len(value)))))


if __name__ == '__main__':
    main(sys.argv[1])
