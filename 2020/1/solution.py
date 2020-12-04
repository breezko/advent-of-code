from itertools import combinations
from functools import reduce


def main(puzzle: list, comb: int) -> int:
    """https://adventofcode.com/2020/day/1"""
    for comb in combinations(puzzle, comb):
        if sum(comb) == 2020:
            print(reduce(lambda x, y: x * y, comb))


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [int(line.strip()) for line in fin.readlines()]
    main(lines, 2)
    main(lines, 3)
