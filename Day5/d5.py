import heapq


def readinput():
    with open("input") as f:
        return [l.strip() for l in f.readlines()]


def convert_to_row_column(bsp):
    row = bsp[0:7].replace('F', '0').replace('B', '1')
    col = bsp[7:10].replace('L', '0').replace('R', '1')
    return int(row, 2), int(col, 2)


def convert_to_seat_id(row, col):
    return row * 8 + col


def get_seat_ids():
    passes = readinput()
    rcs = (convert_to_row_column(bsp) for bsp in passes)
    return [convert_to_seat_id(r, c) for r, c in rcs]


def simple_missing(seatids):
    "2.05 ms ± 27.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)"
    for i in range(min(seatids), max(seatids)):
        if i not in seatids:
            return i


def simple_set(seatids):
    "49.7 µs ± 666 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)"
    seatids = set(seatids)
    for i in range(min(seatids), max(seatids)):
        if i not in seatids:
            return i


def find_missing_seat_sorted(seatids):
    "91.5 µs ± 2.66 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)"
    seatids = sorted(seatids)
    seat = seatids[0]
    for i in seatids:
        if i == seat:
            seat += 1
        else:
            return seat


def find_missing_seat_heap(seatids):
    "189 µs ± 6.77 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)"
    seatids = list(seatids)
    heapq.heapify(seatids)
    seat = heapq.heappop(seatids)
    while (seat + 1) == heapq.heappop(seatids):
        seat = seat + 1
    return seat
