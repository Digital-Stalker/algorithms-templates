from typing import List, Tuple


"""
Без функций
n, a = int(input()), [input().split(), input().split()]
print(*[a[i % 2][i // 2] for i in range(2 * n)])
"""


def zipper(a: List[int], b: List[int]) -> List[int]:
    # Здесь реализация вашего решения
    return [(b[i // 2] if i % 2 else a[i // 2]) for i in range(2 * len(a))]


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
