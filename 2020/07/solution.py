from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys


def main(lines: list) -> None:
    bags = defaultdict(list)
    occurences = defaultdict(list)

    for line in lines:
        colors, v = line.split(" contain ")
        colors = tuple(colors.split()[:-1])
        if v.startswith("no"):
            continue
        bags[colors] = [
            (int(v.split()[0]), tuple(v.split()[1:-1])) for v in v.split(", ")
        ]
        for _, v in bags[colors]:
            occurences[v].append(colors)
    q = deque([("shiny", "gold")])
    s = set([tuple(q[0])])
    while q:
        col = q.popleft()
        for c in occurences[col]:
            if c not in s:
                q.append(c)
                s.add(c)

    print("#1:", len(s) - 1)

    @lru_cache()
    def solve(color):
        ans = 1
        for count, subcol in bags[color]:
            ans += count * solve(subcol)
        return ans

    print("#2:", solve(("shiny", "gold")) - 1)


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    main(lines)
