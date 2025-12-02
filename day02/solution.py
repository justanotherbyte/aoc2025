import re

def is_invalid(n: int):
    ms = (re.findall(r"\b(\d+)\1+\b", str(n)))
    if ms:
        m = ms[0]
        return str(n).count(m) == 2
    
    return False

def is_invalid2(n: int):
    ms = (re.findall(r"\b(\d+)\1+\b", str(n)))
    if ms:
        m = ms[0]
        return str(n).count(m) >= 2
    
    return False


def part1(f: str):
    rs = f.split(",")
    s = 0

    for r in rs:
        a, b = map(int, r.split("-"))

        for n in range(a, b+1):
            if is_invalid(n):
                s += n

    print(s)

def part2(f: str):
    rs = f.split(",")
    s = 0

    for r in rs:
        a, b = map(int, r.split("-"))

        for n in range(a, b+1):
            if is_invalid2(n):
                s += n

    print(s)