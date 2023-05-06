# ID: 86977726
from typing import List


def nearest_zero(n: List[int]) -> List:
    idx_zero = None
    step = 0
    for i in range(len(n)):
        if n[i] != 0 and idx_zero is None:
            n[i] = len(n)
        elif n[i] != 0:
            step += 1
            n[i] = step
        elif n[i] == 0:
            step = 0
            idx_zero = i
    for i in range(len(n) - 1, -1, -1):
        if i > idx_zero:
            continue
        elif n[i] == 0:
            step = 0
        elif n[i] == len(n):
            step += 1
            n[i] = step
        elif n[i] != 0:
            n[i] = min(n[i], n[i + 1] + 1)
    return n


def read_input() -> List[int]:
    street = int(input())
    home = list(map(int, input().strip().split()))
    return home


houses = read_input()
print(' '.join(map(str, nearest_zero(houses))))
