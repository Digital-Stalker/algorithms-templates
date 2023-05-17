# ID: 87175851
def trainer(matrix: str, point: int) -> int:
    nums = {}
    scores = 0

    for count in matrix:
        if count in nums:
            nums[count] += 1
        else:
            nums[count] = 1
    for time in nums.values():
        if time and time <= point + point:
            scores += 1
    return scores


if __name__ == '__main__':
    point = int(input())
    matrix: str = (''.join([input() for _ in range(4)])).replace('.', '')
    print(trainer(matrix, point))
