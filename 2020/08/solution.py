from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
import sys


def main(lines: list) -> None:
    prog = [(op, int(x)) for op, x in lines]

    def rp(prog):
        pc = 0
        acc = 0
        visits = set()
        while pc < len(prog):
            if pc in visits:
                # part 1: return acc
                return None
            visits.add(pc)
            op, v = prog[pc]
            if op == "acc":
                acc += v
                pc += 1
            elif op == "jmp":
                pc += v
            else:
                pc += 1
        return acc

    for i in range(len(prog)):
        if prog[i][0] == "acc":
            continue
        new_op = "jmp" if prog[i][0] == "nop" else "nop"
        new_prog = prog[:i] + [(new_op, prog[i][1])] + prog[i + 1 :]
        x = rp(new_prog)
        if x is not None:
            print(x)


if __name__ == "__main__":
    fin = open("data.in", "r")
    lines = [line.strip().split() for line in fin.readlines() if line.strip()]
    main(lines)
