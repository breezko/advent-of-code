from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys
import timeit
import re


def main(lines: list) -> None:
    """https://adventofcode.com/2020/day/3
    r1 = Part 1 result
    r2 = Part 2 result

    Args:
        lines (list): puzzle input

    Returns:
        tuple: (part1,part2)
    """
    s1, s2, r1, r2, req = 0, 0, 0, 0, 7
    for line in lines:
        words = [i.split(":") for i in line.split()]
        if len(words) < 1:
            cond1 = s1 == req
            cond2 = s2 == req
            r1 += cond1
            r2 += cond2
            s1, s2 = 0, 0
        for i in words:
            k, v = i[0], i[1]
            if k == "byr":
                v = int(v)
                s1 += 1
                s2 += v >= 1920 and v <= 2002
            elif k == "iyr":
                v = int(v)
                s1 += 1
                s2 += v >= 2010 and v <= 2020
            elif k == "eyr":
                v = int(v)
                s1 += 1
                s2 += v >= 2020 and v <= 2030
            elif k == "hgt":
                v2 = int(re.search(r"\d+", v).group())
                s1 += 1
                c2 = re.findall(r"\D+", v)
                s2 += (
                    (c2[0] == "in" and v2 >= 59 and v2 <= 76)
                    or ("cm" == c2[0] and v2 >= 150 and v2 <= 193)
                    if len(c2) > 0
                    else 0
                )
            elif k == "hcl":
                s1 += 1
                s2 += re.search(r"^#[a-f0-9]{6}$", v) != None
            elif k == "ecl":
                s1 += 1
                f = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                s2 += v in f
            elif k == "pid":
                s1 += 1
                s2 += re.search(r"^[0-9]{9}$", v) != None

    r1 += s1 == req
    r2 += s2 == req
    print(r1)
    print(r2)


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [l.strip() for l in fin.readlines()]
    main(lines)
    t = timeit.Timer(stmt="solution.main(lines)", setup="import solution")
    print("TASK: ", t.timer())
