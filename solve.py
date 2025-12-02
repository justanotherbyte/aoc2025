import importlib
import sys


day = int(sys.argv[-1])
name = f"day{day:02}"

mod = importlib.import_module(f"{name}.solution")

if getattr(mod, "USE_SAMPLE", False):
    suffix = "_sample"
else:
    suffix = ""

with open(f"inputs/{name}{suffix}.txt", "r") as f:
    input_text = f.read()



print("Running part 1...")
mod.part1(input_text)

print("Running part 2...")
mod.part2(input_text)