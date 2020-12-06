import string


def readinput():
    with open("input") as f:
        return [l.strip() for l in f.readlines()]


def parse_groups(input_lines, joinfn, initial):
    group = initial
    for l in input_lines:
        if l == '':
            yield group
            group = initial
        else:
            group = joinfn(group, l)
    if len(group):
        yield group


def part1():
    lines = readinput()
    groups = parse_groups(
        lines,
        joinfn=set.union,
        initial=set()
    )
    return sum(len(g) for g in groups)


def part2():
    lines = readinput()
    groups = parse_groups(
        lines,
        joinfn=set.intersection,
        initial=set(string.ascii_lowercase)
    )
    return sum(map(len, groups))
