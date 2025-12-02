import re

def is_invalid(n: int):
    ms = re.findall(r"\b(\d+)\1+\b", str(n))
    if ms:
        m = ms[0]
        return str(n).count(m)
    
    return 0


def part1(f: str):
    s = 0

    for r in f.split(","):
        a, b = map(int, r.split("-"))

        for n in range(a, b+1):
            s += n if is_invalid(n) == 2 else 0

    print(s)

def part2(f: str):
    s = 0

    for r in f.split(","):
        a, b = map(int, r.split("-"))

        for n in range(a, b+1):
            s += n if is_invalid(n) >= 2 else 0

    print(s)