
import logging

from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("d8")


def readinput():
    with open("input") as f:
        return [l.strip() for l in f.readlines()]


class Instruction(object):
    linenumber = 0
    op = None
    arg = None

    def __init__(self, linenumber, line) -> None:
        super().__init__()
        self.op, self.arg = line.split(" ")
        if self.op not in ('acc', 'jmp', 'nop'):
            raise Exception(f"Unknown op on line {linenumber}: {line!r}")
        self.arg = int(self.arg)
        self.linenumber = linenumber

    def __repr__(self):
        return f"{self.linenumber:3}: {self.op} {self.arg}"

    def flip(self):
        if self.op == 'jmp':
            self.op = 'nop'
        elif self.op == 'nop':
            self.op = 'jmp'

    def nextlinenumber(self, flip=False):
        if self.op == 'acc':
            return self.linenumber + 1
        elif (self.op == 'nop' and flip is False):
            return self.linenumber + 1
        elif (self.op == 'jmp' and flip):
            return self.linenumber + 1
        elif (self.op == 'jmp' and flip is False):
            return self.linenumber + self.arg
        elif (self.op == 'nop' and flip):
            return self.linenumber + self.arg

    def execute(self, accumulator):
        if self.op == 'nop':
            logger.debug(
                f"{self.linenumber:3}: nop")
            linenumber = self.linenumber + 1
        elif self.op == 'acc':
            logger.debug(
                f"{self.linenumber:3}: acc {accumulator} + {self.arg}")
            linenumber = self.linenumber + 1
            accumulator += self.arg
        elif self.op == 'jmp':
            logger.debug(
                f"{self.linenumber:3}: jmp {self.arg}")
            linenumber = self.linenumber + self.arg
        else:
            raise Exception(f"Unknown op {self.op!r}")
        return linenumber, accumulator


def parsebootcode(lines):
    for ln, l in enumerate(lines):
        yield Instruction(ln, l)


def run(program):
    accumulator = 0
    linenumber = 0
    visited = set()
    while True:
        if linenumber == len(program):
            return accumulator, None
        elif linenumber > len(program):
            return accumulator, "Bad jump past end of program"
        elif linenumber in visited:
            return accumulator, "Infinite loop"
        nextop = program[linenumber]
        visited.add(linenumber)
        linenumber, accumulator = nextop.execute(accumulator)


def p1():
    lines = readinput()
    program = list(parsebootcode(lines))
    accumulator, err = run(program)
    return accumulator


def findreachable(program, flip=False):
    reachable = defaultdict(set)
    for instr in program:
        reachable[instr.nextlinenumber(flip)].add(instr.linenumber)
    return reachable


def p2():
    lines = readinput()
    program = list(parsebootcode(lines))
    # build graph of how to get to any line
    reachable = findreachable(program)
    # Assume every flippable instruction is flipped, build the same graph
    freachable = findreachable(program, flip=True)

    flippers = []
    def walk(ln, visited=frozenset(), hasflipped=False):
        # We can get to ln from where?
        visited = visited.union([ln])
        possibilities = reachable[ln] - visited
        if 0 in possibilities:
            return True
        if not possibilities and not hasflipped and len(freachable[ln]) == 1:
            # This line would be unreachable but no instructions have been
            # flipped yet and there exists 1 instruction that if flipped would
            # land us here.
            logger.info("Found possible flip of %r", freachable[ln])
            maybeflipln = list(freachable[ln])[0]
            if walk(maybeflipln, visited, True):
                # it looks like it works out, note it for verification
                flippers.append(maybeflipln)
                return True
        else:
            return any(walk(p, visited, hasflipped) for p in possibilities)

    # Starting at the end of the program, how did we get there?
    if walk(len(program)):
        # verify the candidates complete
        for flip in flippers:
            program[flip].flip()
            accumulator, error = run(program)
            if not error:
                logger.info("Flip of %r was it!", flip)
                yield accumulator
            else:
                logger.info("Flip of %r failed to pan out", flip)
                # flip back to try the next one
                program[flip].flip()


def p2brute():
    "Just try flipping every instruction 1 by 1 to see what works"
    lines = readinput()
    program = list(parsebootcode(lines))

    for inst in program:
        inst.flip()
        acc, err = run(program)
        if err is None:
            yield acc
        else:
            logger.info("Flipping %r, failed with %r", inst.linenumber, err)
        inst.flip()
