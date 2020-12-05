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
    """https://adventofcode.com/2020/day/5"""
    seats = []
    for line in lines:
        row_border = 0x80
        column_border = 0x8
        rows = [x for x in range(0, row_border, 1)]
        cols = [x for x in range(0, column_border, 1)]
        for ch in line:
            if ch == "F" or ch == "B":
                row_border //= 2
                rows = rows[:row_border] if ch == "F" else rows[row_border:]
            else:
                column_border //= 2
                cols = cols[column_border:] if ch == "R" else cols[:column_border]

        seats.append(rows[0] * 8 + cols[0])
    print(max(seats))
    seat_lower, seat_upper = min(seats), max(seats)
    for seat_id in range(seat_lower, seat_upper):
        if seat_id not in seats:
            print(seat_id)


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [l.strip() for l in fin.readlines()]
    main(lines)
