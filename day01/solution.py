def part1(f: str):
    n = 50
    c = 0

    for line in f.splitlines():
        direction = line[0]
        steps = int(line[1:])

        steps = steps % 100

        mul = -1 if direction == "L" else 1
        n = (n + (steps * mul)) % 100

        if n == 0:
            c += 1

    print(c)

def part2(f: str):
    n = 50
    c = 0

    for line in f.splitlines():
        direction = line[0]
        steps = int(line[1:])

        iters, steps = divmod(steps, 100)

        mul = -1 if direction == "L" else 1
        t, np = n, (n + (steps * mul))
        
        n = np % 100
        c += iters + (n == 0 or (n != np and t != 0))

    print(c)
