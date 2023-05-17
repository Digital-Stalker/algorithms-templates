# ID: 87175611
from typing import List


def nearest_zero(street: List[int], houses: int) -> List:
    idx_zero = None
    step = 0
    for home in range(houses):
        if street[home] != 0 and idx_zero is None:
            street[home] = houses
        elif street[home] != 0:
            step += 1
            street[home] = step
        elif street[home] == 0:
            step = 0
            idx_zero = home
    for home in range(houses - 1, -1, -1):
        if home > idx_zero:
            continue
        elif street[home] == 0:
            step = 0
        elif street[home] == houses:
            step += 1
            street[home] = step
        elif street[home] != 0:
            street[home] = min(street[home], street[home + 1] + 1)
    return street


if __name__ == '__main__':
    houses = int(input())
    street = [int(num) for num in input().split()]
    print(*nearest_zero(street, houses), sep=' ')
