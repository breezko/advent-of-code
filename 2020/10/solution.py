from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys


def main(lines: list) -> None:
    jolts = {1: 0, 2: 0, 3: 1}
    for i, item in enumerate(lines):
        if i == 0:
            curr = lines[i]
            jolts[curr] += 1
            continue
        diff = item - curr
        if 0 < diff < 4:
            jolts[item - curr] += 1

        curr = lines[i]

    print(jolts[1] * jolts[3])

    a = [0] + lines + [lines[-1] + 3]
    dp = [1]
    for i in range(1, len(a)):
        ans = 0
        for j in range(i):
            if a[j] + 3 >= a[i]:
                ans += dp[j]
        dp.append(ans)
    print(dp[-1])


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = sorted(set(int(line.strip()) for line in fin.readlines() if line.strip()))
    main(lines)
