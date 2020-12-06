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
    """https://adventofcode.com/2020/day/6"""
    ans1, ans2 = 0, 0
    group = set()
    person = []
    char_dict = {}
    ans2 = 0
    for line in lines:
        duplicates = 0
        if not line or line == lines[-1]:
            ans1 += len(group)
            group = set()
            for p in person:
                for op in p:
                    if op in char_dict:
                        char_dict[op] += 1
                    else:
                        char_dict[op] = 1

            for k, _ in char_dict.items():
                if char_dict[k] == len(person):
                    duplicates += 1
            ans2 += duplicates
            person = []
            char_dict = {}
            continue
        person.append([char for char in line])
        for char in line:
            group.add(char)

    print(ans2)
    print(ans1)


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [l.strip() for l in fin.readlines()]
    main(lines)
