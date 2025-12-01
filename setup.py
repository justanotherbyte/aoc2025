import sys
import os

import requests


TEMPLATE = """def part1(f: str): ...

def part2(f: str): ...
"""

def download_input(day: int):
    with open(".session", "r") as f:
        cookie = f.read()
    
    url = f"https://adventofcode.com/2025/day/{day}/input"
    cookies = {"session": cookie}
    r = requests.get(url, cookies=cookies)

    r.raise_for_status()

    with open(f"inputs/day{day:02}.txt", "w+") as f:
        f.write(r.text)

def setup_solution(day: int):
    os.mkdir(f"day{day:02}")
    with open(f"day{day:02}/solution.py", "w+") as f:
        f.write(TEMPLATE)

day = int(sys.argv[-1])
download_input(day)
setup_solution(day)