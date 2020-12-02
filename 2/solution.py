from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys
import timeit

def main(lines: list) -> tuple:
    """https://adventofcode.com/2020/day/2
    r1 = Part 1 result
    r2 = Part 2 result

    Args:
        lines (list): puzzle input

    Returns:
        tuple: (part1,part2)
    """
    r1,r2 = 0, 0
    for line in lines:
        a,b,c = line.split()
        b = b[0]
        lo, hi = map(int,a.split("-"))
        r1 += lo <= c.count(b) <= hi
        r2 += sum(c[x - 1] == b for x in (lo, hi)) == 1
    print(r1)
    print(r2)
    return (r1,r2)

if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    main(lines)
    t = timeit.Timer(stmt="solution.main(lines)", setup="import solution")
    print("TASK: ", t.timer())
    