#!/usr/bin/env python3
# coding: utf-8


import os
import string
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def splitInHalf(text):
    firstpart, secondpart = text[:len(text)//2], text[len(text)//2:]
    return (firstpart, secondpart)


def getPriority(item):
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    return alphabet.find(item) + 1


def part1(data):
    print('part1:')
    total = 0
    for line in data:
        firstpart, secondpart = splitInHalf(line)
        common = ''.join(set(firstpart).intersection(set(secondpart)))
        total += getPriority(common)
    print(total)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def part2(data):
    print('part2:')
    total = 0
    for chunk in chunks(data, 3):
        common = ''.join(set(chunk[0]).intersection(chunk[1]).intersection(chunk[2]))
        total += getPriority(common)
    print(total)


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        part1(data) # 7903
        part2(data) # 2548


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
