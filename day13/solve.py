#! /usr/bin/python3
import sys


def parse_input(path):
    layers = []
    for line in open(path):
        if line.strip():
            k, v = line.split(':')
            layers.append( (int(k), int(v)) )
    return layers


def make_trip(layers):
    severity = 0
    for depth, scan_range in layers:
        if not depth % ((scan_range - 1) * 2):
            severity += depth * scan_range
    return severity


def make_all_trips(layers):
    start_time = 0
    periods = [(depth, (scan_range - 1) * 2) for depth, scan_range in layers]
    while True:
        for depth, period in periods:
            t = depth + start_time
            if not t % period:
                break
        else:
            break
        start_time += 1
    return start_time


def main(input_file):
    layers = parse_input(input_file)
    print("Part 1:", make_trip(layers))
    print("Part 1:", make_all_trips(layers))


if __name__ == '__main__':
    main(sys.argv[1])
