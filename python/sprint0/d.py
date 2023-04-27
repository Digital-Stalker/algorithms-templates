from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    # Здесь реализация вашего решения
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                return arr[i], arr[j]
    # По условию задачи пара обязательно должна найтись.
    # Но предусмотрительность не помешает:
    # если пара не найдена - вернём None, None (или можно выкинуть exception).
    return None


def twosum_with_sort(numbers, X):
    # Сортируем исходный массив стандартной функцией.
    numbers.sort()

    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == X:
            return numbers[left], numbers[right]
        if current_sum < X:
            left += 1
        else:
            right -= 1
    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
    return None


def twosum_extra_ds(numbers, X):
    # Создаём вспомогательную структуру данных с быстрым поиском элемента.
    previous = set()

    for A in numbers:
        Y = X - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    # Если ничего не нашлось в цикле, значит, нужной пары элементов в массиве нет.
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input()
print_result(twosum_extra_ds(arr, target_sum))
