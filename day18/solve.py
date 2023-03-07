#! /usr/bin/python3
import sys
import string


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
        self.regs = {reg: 0 for reg in string.ascii_lowercase}
        self.inputs = []
        self.outputs = []
        self.ip = 0
        self.snd_count = 0

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
            elif op == 'add':
                self.regs[args[0]] += self.value(args[1])
            elif op == 'mul':
                self.regs[args[0]] *= self.value(args[1])
            elif op == 'mod':
                self.regs[args[0]] %= self.value(args[1])
            elif op == 'jgz':
                if self.value(args[0]) > 0:
                    self.ip += self.value(args[1]) - 1
            elif op == 'snd':
                self.outputs.append(self.value(args[0]))
                self.snd_count += 1
            elif op == 'rcv':
                if not self.inputs:
                    return
                self.regs[args[0]] = self.inputs.pop(0)
            self.ip += 1


def main(input_file):
    insns = parse_input(input_file)

    p = Prog(insns)
    p.run()
    print("Part 1:", p.outputs[-1])

    p1 = Prog(insns)
    p2 = Prog(insns)
    p1.regs['p'] = 0
    p1.inputs = p2.outputs
    p2.regs['p'] = 1
    p2.inputs = p1.outputs
    while True:
        p1.run()
        p2.run()
        if not (p1.outputs or p2.outputs):
            break
    print("Part 2:", p2.snd_count)


if __name__ == '__main__':
    main(sys.argv[1])
