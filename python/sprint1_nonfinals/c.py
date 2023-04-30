from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    # Здесь реализация вашего решения
    top_idx = (row - 1, col)
    right_idx = (row, col + 1)
    bot_idx = (row + 1, col)
    left_idx = (row, col - 1)

    idx_list = [
        top_idx,
        right_idx,
        bot_idx,
        left_idx
    ]

    res = []
    for idx in idx_list:
        row_idx = idx[0]
        col_idx = idx[1]
        if row_idx >= 0 and col_idx >= 0:
            neighbour = matrix[row_idx][col_idx]
            res.append(neighbour)
    return sorted(res)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
