def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    binary = ''
    _divisible = 0
    if number == 0:
        binary = '0'
    if number == 1:
        binary = '1'
    if number > 1:
        while number > 0:
            _divisible = number % 2
            number = number // 2
            if _divisible > 0:
                binary += '1'
            if _divisible == 0:
                binary += '0'

    return binary[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
