from itertools import combinations
import math


def main(puzzle: list) -> int:
    res = res2 = []
    for line in puzzle:
        res.append(math.floor(line / 3 - 2))

    for item in res:
        amt = item
        module = []
        while amt >= 0:
            module.append(amt)
            amt = math.floor(amt / 3 - 2)
        res2.append(sum(module))

    print(sum(res))
    print(sum(res2))


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [int(line.strip()) for line in fin.readlines()]
    main(lines)
