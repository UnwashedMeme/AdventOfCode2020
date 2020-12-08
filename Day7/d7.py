import re
import logging

from functools import lru_cache

logging.basicConfig(level=logging.DEBUG)


def readinput():
    with open("input") as f:
        return [l.strip() for l in f.readlines()]


def readrules():
    containers = {}
    for l in readinput():
        try:
            if l == "": continue
            outer, innerclause = l.split(" bags contain ")
            if innerclause == "no other bags.":
                inner = []
            else:
                inner = re.findall("(\d) ([^.,]*) bags?", innerclause)
            if outer in containers:
                raise Exception(f"Already have a rule for {outer!r}")
            containers[outer] = inner
        except Exception:
            logging.error(f"Failed parsing: {l!r}")
            raise
    return containers




def countif(predicate, iterable):
    return sum(1 for item in iterable if predicate(item))


def how_many_goldholders(containers):

    def can_contain_gold(c):
        innerbags = [i[1] for i in containers[c]]
        if len(innerbags) == 0:
            return False
        elif "shiny gold" in innerbags:
            return True
        else:
            return any(can_contain_gold(c) for c in innerbags)
    return countif(can_contain_gold, containers.keys())


def count_bags_in(bag, containers):
    count = 1
    for ic, inner in containers[bag]:
        count += int(ic) * count_bags_in(inner, containers)
    return count


def p2():
    containers = readrules()
    totalbags = count_bags_in('shiny gold', containers)
    return totalbags - 1  # ignore the shinygold bag
