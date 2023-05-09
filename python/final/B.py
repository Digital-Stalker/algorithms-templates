# ID: 87053928
# Здесь так же стал больше и работать дольше
from typing import List


def trainer(matrix: List[str], point: int) -> int:
    nums = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
            '6': 0, '7': 0, '8': 0, '9': 0, '0': 0}
    scores = 0
    for vl in matrix:
        if vl in nums:
            nums[vl] += 1
        else:
            nums[vl] = 1
    for t in range(1, 10):
        if nums[str(t)] and nums[str(t)] <= point * 2:
            scores += 1
    return scores


if __name__ == '__main__':
    point = int(input())
    matrix = list((''.join([input() for _i in range(4)])).replace('.', ''))
    print(trainer(matrix, point))
