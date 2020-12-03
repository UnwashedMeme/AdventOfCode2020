import re


def p1(line):
    m = re.match(r'(\d+)-(\d+) (.): (.*)', line)
    lower, upper, char, password = m.groups()
    limits = range(int(lower), int(upper) + 1)
    return password.count(char) in limits


def p2(line):
    m = re.match(r'(\d+)-(\d+) (.): (.*)', line)
    p1, p2, char, password = m.groups()
    c1 = password[int(p1) - 1]
    c2 = password[int(p2) - 1]
    return (c1 == char) != (c2 == char)


def readinput():
    with open("input") as f:
        return f.readlines()


def countgood(p):
    lines = readinput()
    return sum(1 for l in lines if p(l))
