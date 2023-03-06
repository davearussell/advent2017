#! /usr/bin/python3
import sys


def is_valid(phrase, allow_anagrams=True):
    if not allow_anagrams:
        phrase = [''.join(sorted(word)) for word in phrase]
    return len(set(phrase)) == len(phrase)


def main(input_file):
    phrases = [line.split() for line in open(input_file)]
    print("Part 1:", len([phrase for phrase in phrases if is_valid(phrase)]))
    print("Part 2:", len([phrase for phrase in phrases if is_valid(phrase, False)]))


if __name__ == '__main__':
    main(sys.argv[1])
