import logging
import re


def validate_hgt(v):
    """
    hgt (Height) - a number followed by either cm or in:

    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    if v.endswith("cm"):
        return int(v.strip("cm")) in range(150, 194)
    elif v.endswith("in"):
        return int(v.strip("in")) in range(59, 77)
    else:
        return False


def validate_hcl(v):
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    return v and re.match(r"^#[0-9a-f]{6}$", v)


def validate_ecl(v):
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    return v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_pid(v):
    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    return re.match(r"^[0-9]{9}$", v)


def validate_cid(v):
    """
    cid (Country ID) - an integer
    """
    try:
        return int(v)
    except Exception:
        return False


REQUIRED = {
    "byr": lambda v: int(v) in range(1920, 2003),  # (Birth Year)
    "iyr": lambda v: int(v) in range(2010, 2021),  # (Issue Year)
    "eyr": lambda v: int(v) in range(2020, 2031),  # (Expiration Year)
    "hgt": validate_hgt,  # (Height)
    "hcl": validate_hcl,  # (Hair Color)
    "ecl": validate_ecl,  # (Eye Color)
    "pid": validate_pid,  # (Passport ID)
    #"cid": validate_cid   # "cid",  # (Country ID)
}


def readpassports():
    """
    Passport data is validated in batch files (your puzzle input). Each
    passport is represented as a sequence of key:value pairs separated by
    spaces or newlines. Passports are separated by blank lines.
    """
    with open('input') as f:
        d = {}
        for line in f:
            line = line.strip()
            try:
                if line == "":
                    yield d
                    d = {}
                else:
                    pieces = re.split(r"\s", line)
                    for p in pieces:
                        key, value = p.split(":")
                        d[key] = value
            except Exception:
                logging.fatal("Failed parsing %r", line)
        if len(d):
            yield d


def countif(predicate, iterable):
    return sum(1 for item in iterable if predicate(item))


def validate(passport):
    for key, validator in REQUIRED.items():
        value = passport.get(key)
        if not value:
            logging.warning(
                "Passport validation failed, no %r for %r",
                key, passport)
            return False
        elif not validator(value):
            logging.warning(
                "Passport validation failed, on %r for %r",
                key, passport)
            return False
    return True


def countvalid(passports):
    return countif(validate, passports)
