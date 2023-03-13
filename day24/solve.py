#! /usr/bin/python3
import sys


def parse_input(path):
    parts = set()
    for line in open(path):
        if line.strip():
            a, b = [int(x) for x in line.split('/')]
            parts.add(tuple(sorted((a, b))))
    return parts


def choose_parts(all_parts):
    done = []
    doing = [([part], part[1]) for part in all_parts if part[0] == 0]
    while doing:
        next_doing = []
        for bridge, need_port in doing:
            available = all_parts - set(bridge)
            candidates = [ part for part in available if need_port in part]
            if candidates:
                for part in candidates:
                    end_port = part[0] if part[1] == need_port else part[1]
                    next_doing.append((bridge + [part], end_port))
            else:
                done.append((sum(map(sum, bridge)), len(bridge), bridge))
        doing = next_doing
    return done
                

def main(input_file):
    parts = parse_input(input_file)
    bridges = choose_parts(parts)

    bridges.sort(key=lambda bridge: bridge[0]) # sort by strength
    print("Part 1:", bridges[-1][0])

    bridges.sort(key=lambda bridge: bridge[1]) # sort by length
    print("Part 2:", bridges[-1][0])


if __name__ == '__main__':
    main(sys.argv[1])
