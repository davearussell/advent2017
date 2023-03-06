#! /usr/bin/python3
import operator
import sys


def parse_input(path):
    cmps = {
        '<': operator.lt,
        '<=': operator.le,
        '!=': operator.ne,
        '==': operator.eq,
        '>=': operator.ge,
        '>': operator.gt,
    }
    insns = []
    for line in open(path):
        if not line.strip():
            continue
        reg, op, val, _, cmpreg, cmpop, cmpval = line.split()
        val = int(val)
        if op == 'dec':
            val = -val
        cmpval = int(cmpval)
        insns.append((reg, val, cmpreg, cmps[cmpop], cmpval))
    return insns


def run(insns):
    regs = {}
    max_val = None
    for reg, val, cmpreg, cmpfn, cmpval in insns:
        if cmpfn(regs.get(cmpreg, 0), cmpval):
            regs[reg] = regs.get(reg, 0) + val
            if max_val is None or regs[reg] > max_val:
                max_val = regs[reg]
    return max(regs.values()), max_val


def main(input_file):
    insns = parse_input(input_file)
    part1, part2 = run(insns)
    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == '__main__':
    main(sys.argv[1])
