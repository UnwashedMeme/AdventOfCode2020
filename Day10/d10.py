from collections import Counter
from itertools import chain, combinations, count


def readinput():
    with open("input") as f:
        return [int(l.strip()) for l in f.readlines()]


def p1():
    c = Counter()
    joltadapters = sorted(readinput())
    devicejoltage = joltadapters[-1] + 3
    joltadapters.append(devicejoltage)
    jolts = 0
    for ja in joltadapters:
        delta = ja - jolts
        c[delta] += 1
        jolts = ja

    assert max(c.keys()) <= 3
    return c


def p2(joltadapters=None):
    if not joltadapters:
        joltadapters = sorted(readinput())

    devicejoltage = joltadapters[-1] + 3
    joltadapters.append(devicejoltage)
    jolts = 0
    combos = 1
    group = [0]
    for ja in joltadapters:
        delta = ja - jolts
        if delta == 3:
            logging.info("Counting subgroup %r: %r", group, countpaths(group))
            combos *= countpaths(group)
            group = [ja]
        else:
            group.append(ja)
        jolts = ja

    return combos


def countpaths(l):
    if len(l) >= 4 and l[3] - l[0] == 3:
        return countpaths(l[1:]) \
            + countpaths(l[2:]) \
            + countpaths(l[3:])
    if len(l) >= 3 and l[2] - l[0] <= 3:
        return countpaths(l[1:]) + countpaths(l[2:])
    if len(l) >= 2:
        return countpaths(l[1:])
    return 1


def enumpaths(l):
    if len(l) >= 4 and l[3] - l[0] == 3:
        continuations = chain(
            enumpaths(l[1:]),
            enumpaths(l[2:]),
            enumpaths(l[3:])
        )
        for c in continuations:
            yield [l[0]] + c

    elif len(l) >= 3 and l[2] - l[0] <= 3:
        continuations = chain(
            enumpaths(l[1:]),
            enumpaths(l[2:])
        )
        for c in continuations:
            yield [l[0]] + c
    elif len(l) >= 2:
        for c in enumpaths(l[1:]):
            yield [l[0]] + c
    else:
        yield l
