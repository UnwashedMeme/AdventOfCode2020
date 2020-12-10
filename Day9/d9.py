import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("d9")


def readinput():
    with open("input") as f:
        return [int(l.strip()) for l in f.readlines()]


def calc_sums(group):
    def looper():
        for idx, i in enumerate(group[:-1]):
            for j in group[idx+1:]:
                yield i + j
    return set(looper())


def p1():
    xmas_data = readinput()
    for idx, i in enumerate(xmas_data[25:], 25):
        logger.debug(f'Checking {idx}: {i}')
        previous_sums = calc_sums(xmas_data[idx-25:idx])
        if i not in previous_sums:
            return i


def p2():
    xmas_data = readinput()
    target = p1()
    for iidx, i in enumerate(xmas_data):
        sum = i
        for jidx, j in enumerate(xmas_data[iidx+1:], iidx+1):
            sum += j
            if sum == target:
                logger.info(f'found match in {iidx}, {jidx}')
                group = xmas_data[iidx:jidx+1]
                return min(group) + max(group)
            elif sum > target:
                break
