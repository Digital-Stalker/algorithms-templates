def counting_sort(array):
    pink = []
    yellow = []
    raspberry = []
    for color in array:
        if color == 0:
            pink.append(color)
        elif color == 1:
            yellow.append(color)
        elif color == 2:
            raspberry.append(color)
    return ' '.join(map(str, (pink + yellow + raspberry)))


if __name__ == '__main__':
    items = int(input())
    colors = [int(_) for _ in input().split()]
    print(counting_sort(colors))
