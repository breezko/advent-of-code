from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys


def main(lines: list) -> None:
    root = deque(lines)
    CHUNK_SIZE = 25
    preamble = deque(lines[:CHUNK_SIZE])
    lines = deque(lines[CHUNK_SIZE:])
    while True:
        ans1 = lines.popleft()
        for comb in itertools.combinations(preamble, 2):
            s = sum(comb)
            if s == ans1:
                preamble.popleft()
                preamble.append(ans1)
                break
        if s != ans1:
            break

    while True:
        window_sum = 0
        items = []
        for i in range(len(root)):
            items.append(root[i])
            window_sum = sum(items)
            if window_sum > ans1:
                items.clear()
                root.popleft()
                break
            if window_sum == ans1:
                break

        if window_sum == ans1:
            ans2 = min(items) + max(items)
            break
    print(ans1, ans2)


if __name__ == "__main__":

    fin = open("data.in", "r")
    lines = [int(line.strip()) for line in fin.readlines() if line.strip()]
    main(lines)
