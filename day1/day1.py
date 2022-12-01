#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def part1(sums):
    print('part1:')

    print(max(sums))


def part2(sums):
    print('part2:')

    top3 = sorted(sums, reverse=True)[:3]
    print(sum(top3))


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read()
        data = data.split("\n\n")
        elves = []
        for idx, d in enumerate(data):
            elfData = d.split("\n")
            elfData = sum([int(food) for food in elfData])
            elves.append(elfData)

        part1(elves) # 72511
        part2(elves) # 212117


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
