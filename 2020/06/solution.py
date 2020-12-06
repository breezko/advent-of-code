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
    persons = []
    char_dict = {}
    ans2 = 0
    for line in lines:
        duplicates = 0
        if not line or line == lines[-1]:
            ans1 += len(group)
            group = set()
            for p in persons:
                for op in p:
                    char_dict[op] = char_dict[op] + 1 if op in char_dict else 1

            for k, _ in char_dict.items():
                if char_dict[k] == len(persons):
                    duplicates += 1
            ans2 += duplicates
            persons = []
            char_dict = {}
            continue
        persons.append([char for char in line])
        for char in line:
            group.add(char)

    print(ans2)
    print(ans1)


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [l.strip() for l in fin.readlines()]
    main(lines)
