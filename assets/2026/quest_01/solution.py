import math

def part_1(data: str) -> int | str | None:
    data = list(map(int, data.split(",")))
    missings = 0
    for n in data:
        s = math.isqrt(n)
        if s * s < n:
            s += 1
        missings += s * s - n 
    return missings


def part_2(data: str) -> int | str | None:
    lines = data.splitlines()
    return None  # TODO


def part_3(data: str) -> int | str | None:
    lines = data.splitlines()
    return None  # TODO
