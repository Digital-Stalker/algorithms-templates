from typing import List


def merge(arr: list, lf: int, mid: int, rg: int) -> List:
    # Your code
    # “ヽ(´▽｀)ノ”
    result = []
    left = arr[lf:mid]
    right = arr[mid:rg]
    l = r = 0
    while len(result) < len(left) + len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
        if r == len(right):
            result += left[l:]
            break
        if l == len(left):
            result += right[r:]
            break
    return result


def merge_sort(arr: list, lf: int, rg: int) -> None:
    # Your code
    # “ヽ(´▽｀)ノ”
    if rg - lf >= 2:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
