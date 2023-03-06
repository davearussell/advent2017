#! /usr/bin/python3
import sys


def run(jumps, part2=False):
    i = steps = 0
    while 0 <= i < len(jumps):
        v = jumps[i]
        jumps[i] += (-1 if (part2 and v >= 3) else 1)
        i += v
        steps += 1
    return steps


def main(input_file):
    jumps = [int(x) for x in open(input_file).read().split()]
    print("Part 1:", run(jumps.copy()))
    print("Part 2:", run(jumps.copy(), True))
        
        


if __name__ == '__main__':
    main(sys.argv[1])
