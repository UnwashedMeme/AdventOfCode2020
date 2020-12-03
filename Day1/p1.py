#!/bin/python3

def readinput():
    with open("input") as f:
        return [int(line) for line in f]


def find2020p1(input):
    for idx in range(0, len(input) - 1):
        i = input[idx]
        for idx2 in range(idx+1, len(input)):
            j = input[idx2]
            if i + j == 2020:
                return i * j


def find2020p2(input):
    for idx in range(0, len(input) - 2):
        i = input[idx]
        for idx2 in range(idx + 1, len(input) - 1):
            j = input[idx2]
            if i + j > 2020:
                continue
            for idx3 in range(idx2 + 1, len(input)):
                k = input[idx3]
                if i + j + k == 2020:
                    return i * j * k
