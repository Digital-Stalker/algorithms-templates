def get_big_digit(num, dgt):
    for i in range(num - 1):
        for j in range(0, num - i - 1):
            var1 = dgt[j] + dgt[j + 1]
            var2 = dgt[j + 1] + dgt[j]
            if var1 < var2:
                dgt[j], dgt[j + 1] = dgt[j + 1], dgt[j]
    print(''.join(dgt))


if __name__ == '__main__':
    counts = int(input())
    digits = input().split(' ')
    get_big_digit(counts, digits)
