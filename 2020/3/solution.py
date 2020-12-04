from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys
import timeit


def main(lines: list) -> None:
    """https://adventofcode.com/2020/day/3"""
    r2 = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    ph, pw = 0, 0
    for width, height in slopes:
        r1 = 0
        ph, pw = 0, 0
        while ph < len(lines):
            r1 += lines[ph % len(lines)][pw % len(lines[0])] == "#"
            pw += width
            ph += height
        print(r1)
        r2 *= r1
    print(r2)


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [line.strip() for line in fin.readlines()]
    main(lines)
