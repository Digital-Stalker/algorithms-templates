from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    # Здесь реализация вашего решения
    h = 1
    if len(temperatures) == 1:
        return h
    else:
        h = 0
        if len(set(temperatures)) == 1:
            return h
        else:
            if temperatures[0] > temperatures[1]:
                h += 1
            if temperatures[len(temperatures) - 1] > temperatures[len(temperatures) - 2]:
                h += 1
            for n in range(1, len(temperatures) - 1):
                try:
                    if temperatures[n-1] < temperatures[n] > temperatures[n+1]:
                        h += 1
                except IndexError:
                    pass
    return h


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
