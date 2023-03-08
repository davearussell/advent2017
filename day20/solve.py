#! /usr/bin/python3
import re
import sys

import numba
import numpy


# To get the right answers on my input, I needed to simulate 20 steps for
# part 1 and 39 for part 2.
MAX_TIME = 100


def parse_input(path):
    coord = "<(.+),(.+),(.+)>"
    pat = re.compile("p=%s, v=%s, a=%s" % (coord, coord, coord))
    particles = []
    for line in open(path):
        if line.strip():
            values = [int(x) for x in pat.match(line).groups()]
            particles.append((
                len(particles),
                numpy.array(values[:3], dtype=numpy.int32),
                numpy.array(values[3:6], dtype=numpy.int32),
                numpy.array(values[6:], dtype=numpy.int32),
            ))
    return particles


def manhattan_accel(particle):
    _, p, v, a = particle
    return sum(map(abs, a))


def long_term_dist(p, v, a, n):
    for i in range(n):
        v += a
        p += v
    return sum(map(abs, p))


def find_closest_particle(particles):
    # In the long run, the closest particle will be one with minimal acceleration,
    # so we can save time by only considering such particules.
    min_accel = None
    min_dist = None
    min_i = None
    for i, p, v, a in sorted(particles, key=manhattan_accel):
        accel = sum(map(abs, a))
        if min_accel is None:
            min_accel = accel
        elif accel > min_accel:
            break
        dist = long_term_dist(p.copy(), v.copy(), a, MAX_TIME)
        if min_dist is None or dist < min_dist:
            min_dist = dist
            min_i = i
    return min_i


def simulate_collisions(particles):
    for t in range(MAX_TIME):
        for _, _, v, a in particles:
            v += a
        for axis in [0, 1, 2]:
            positions = {}
            for i, p, v, _ in particles:
                p[axis] += v[axis]
                positions[tuple(p)] = positions.get(tuple(p), 0) + 1
            particles = [x for x in particles if positions.get(tuple(x[1])) == 1]
    return len(particles)


def main(input_file):
    particles = parse_input(input_file)
    print("Part 1:", find_closest_particle(particles))
    print("Part 2:", simulate_collisions(particles))


if __name__ == '__main__':
    main(sys.argv[1])
