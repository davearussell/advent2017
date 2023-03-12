#! /usr/bin/python3
import sys


def parse_input(path):
    insns = []
    for line in open(path):
        spl = line.split()
        if spl:
            op, args = spl[0], spl[1:]
            for i in range(len(args)):
                try:
                    args[i] = int(args[i])
                except ValueError:
                    pass
            insns.append((op, args))
    return insns


class Prog:
    def __init__(self, insns):
        self.insns = insns
        self.regs = {reg: 0 for reg in 'abcdefgh'}
        self.ip = 0
        self.mul_count = 0

    def value(self, x):
        if isinstance(x, int):
            return x
        return self.regs[x]

    def run(self):
        freq = 0
        while 0 <= self.ip < len(self.insns):
            op, args = self.insns[self.ip]
            if op == 'set':
                self.regs[args[0]] = self.value(args[1])
            elif op == 'sub':
                self.regs[args[0]] -= self.value(args[1])
            elif op == 'mul':
                self.mul_count += 1
                self.regs[args[0]] *= self.value(args[1])
            elif op == 'jnz':
                if self.value(args[0]) != 0:
                    self.ip += self.value(args[1]) - 1
            self.ip += 1


def count_composites(lo, hi, step):
    composites = set()
    for i in range(2, hi):
        if i not in composites:
            for j in range(2, (hi // i) + 1):
                composites.add(i * j)
    return len(composites & set(range(lo, hi + step, step)))


def main(input_file):
    insns = parse_input(input_file)
    p = Prog(insns)
    p.run()
    print("Part 1:", p.mul_count)

    # The code counts the number of non-primes in a range.
    # The only difference between part 1 and 2 is the size of the range.
    lo = 65 * 100 + 100000
    hi = lo + 17000
    step = 17
    print("Part 2:", count_composites(lo, hi, step))


if __name__ == '__main__':
    main(sys.argv[1])
