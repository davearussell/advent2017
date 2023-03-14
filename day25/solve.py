#! /usr/bin/python3
import re
import sys
import yaml

INIT_PAT = re.compile(r"Begin in state ([A-Z])")
STEPS_PAT = re.compile(r"checksum after (\d+) steps")


def parse_input(path):
    data = open(path).read()
    init, state_text = data.split('\n\n', 1)
    state = INIT_PAT.search(init).group(1)
    n = int(STEPS_PAT.search(init).group(1))
    for text in ['.', 'In state ', 'If the current value is ', 'Write the value ',
                 'Move one slot to the ',
                 'Continue with state ']:
        state_text = state_text.replace(text, '')
    for direction, offset in [('left', '-1'), ('right', '1')]:
        state_text = state_text.replace(direction, offset)
    rules = yaml.safe_load(state_text)
    return state, rules, n


def run(state, rules, n):
    addr = 0
    mem = {}
    for i in range(n):
        mem[addr], direction, state = rules[state][mem.get(addr, 0)]
        addr += direction
    return sum(mem.values())


def main(input_file):
    state, rules, n = parse_input(input_file)
    print("Part 1:", run(state, rules, n))


if __name__ == '__main__':
    main(sys.argv[1])
