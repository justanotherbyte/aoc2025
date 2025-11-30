import importlib
import sys


day = int(sys.argv[-1])
name = f"day{day:02}"

mod = importlib.import_module(f"{name}.solution")

with open(f"inputs/{name}.txt", "r") as f:
    input_text = f.read()

print("Running part 1...")
mod.part1(input_text)

print("Running part 2...")
mod.part2(input_text)