import re


def p1(line):
    """
    Each line gives the password policy and then the password. The password
    policy indicates the lowest and highest number of times a given letter
    must appear for the password to be valid. For example, 1-3 a means that
    the password must contain a at least 1 time and at most 3 times.
    """
    m = re.match(r'(\d+)-(\d+) (.): (.*)', line)
    lower, upper, char, password = m.groups()
    limits = range(int(lower), int(upper) + 1)
    return password.count(char) in limits


def p2(line):
    """
    Each policy actually describes two positions in the password, where 1
    means the first character, 2 means the second character, and so on. (Be
    careful; Toboggan Corporate Policies have no concept of "index zero"!)
    Exactly one of these positions must contain the given letter. Other
    occurrences of the letter are irrelevant for the purposes of policy
    enforcement.
    """
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
