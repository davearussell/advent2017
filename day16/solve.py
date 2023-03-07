#! /usr/bin/python3
import string
import sys


def dance(_dancers, moves):
    dancers = list(_dancers)
    for move in moves:
        op, args = move[0], move[1:]
        if op == 'x':
            a, b = [int(x) for x in args.split('/')]
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif op == 'p':
            x, y = args.split('/')
            a = dancers.index(x)
            b = dancers.index(y)
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif op == 's':
            n = int(args)
            dancers = dancers[-n:] + dancers[:-n]
        else:
          assert 0, move
    return ''.join(dancers)


def main(input_file):
    moves = open(input_file).read().strip().split(',')
    dancers = string.ascii_lowercase[:16]

    seen = {}
    states = [dancers]

    target_i = 10 ** 9
    i = 0
    while True:
        dancers = dance(dancers, moves)
        states.append(dancers)
        i += 1
        if i == 1:
            print("Part 1:", dancers)
        if dancers in seen:
            old_i = seen[dancers]
            rem = (target_i - i) % (i - old_i)
            print("Part 2:", states[rem + old_i])
            break
        seen[dancers] = i


if __name__ == '__main__':
    main(sys.argv[1])
