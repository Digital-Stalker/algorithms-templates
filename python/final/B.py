from typing import List, Tuple


def trainer(k, matrix) -> int:
    keys = []
    scores = 0
    for i in range(4):
        for n in matrix[i]:
            if n == '.':
                continue
            keys.append(int(n))
    for i in range(1, 10):
        if 0 < keys.count(i) <= 2 * k:
            scores += 1
    return scores


def read_input() -> Tuple[int, List[str]]:
    k = int(input())
    matrix = [str(input()) for i in range(4)]
    return k, matrix


k, matrix = read_input()
print(trainer(k, matrix))
