import logging


def readinput():
    with open("input") as f:
        return [l.strip() for l in f.readlines()]


def treesfound(field, right=3, down=1):
    x, y = 0, 0
    trees = 0
    fieldwidth = len(field[0])
    fieldlength = len(field)
    while y < fieldlength:
        char = field[y][x]
        if char == "#":
            trees += 1
        x = (x + right) % fieldwidth
        y = y + down
    logging.info("Slope right %r, down %r found %r trees",
                 right, down, trees)
    return trees


def findall():
    field = readinput()
    return \
        treesfound(field, right=1, down=1) * \
        treesfound(field, right=3, down=1) * \
        treesfound(field, right=5, down=1) * \
        treesfound(field, right=7, down=1) * \
        treesfound(field, right=1, down=2)
