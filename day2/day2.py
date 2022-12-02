#!/usr/bin/env python3
# coding: utf-8


import os
import time


dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def getScoreOfGame(opponent, me):
    moveMap = {
        "X": "rock", "Y": "paper", "Z": "scissors", 
        "A": "rock", "B": "paper", "C": "scissors"
    }

    opponent = moveMap[opponent]
    me = moveMap[me]
    res = 0
    if me == "rock":
        res += 1
    elif me == "paper":
        res += 2
    elif me == "scissors":
        res += 3

    if opponent == me:
        res += 3

    match (me, opponent):
        case ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock"):
            res += 6

    return res


def getCorrectMove(opponent, result):
    myMove = ""
    match (opponent, result):
        case ("A", "X") | ("B", "Z") | ("C", "Y"):
            myMove = "Z"
        case ("B", "X") | ("A", "Y") | ("C", "Z"):
            myMove = "X"
        case ("C", "X") | ("A", "Z") | ("B", "Y"):
            myMove = "Y"

    return (opponent, myMove)



def part1(data):
    print('part1:')
    total = 0
    for line in data:
        opponent, me = line.split()
        total += getScoreOfGame(opponent, me)
    print(total)


def part2(data):
    print('part2:')
    total = 0
    for line in data:
        opponent, result = line.split()
        opponent, me = getCorrectMove(opponent, result)
        total += getScoreOfGame(opponent, me)
    print(total)


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)
    with open(inputfile) as f:
        data = f.read().splitlines()
        part1(data) # 10816
        part2(data) # 11657


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
