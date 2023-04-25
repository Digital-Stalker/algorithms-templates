from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    # Здесь реализация вашего решения
    result = []
    for begin_index in range(0, len(arr) - window_size + 1):
        end_index = begin_index + window_size
        # Просматриваем окно шириной window_size.
        current_sum = 0
        for v in arr[begin_index:end_index]:
            current_sum += v
        current_avg = current_sum / window_size
        result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
