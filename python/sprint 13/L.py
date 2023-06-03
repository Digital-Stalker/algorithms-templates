def get_shopping_day(bank, cost, left, right):
    if right <= left != 0:
        return -1
    mid = (left + right) // 2
    if bank[mid] >= cost and (bank[mid - 1] < cost or mid == 0):
        return mid + 1
    elif cost <= bank[mid]:
        return get_shopping_day(bank, cost, left, mid)
    else:
        return get_shopping_day(bank, cost, mid + 1, right)


if __name__ == '__main__':
    days = int(input())
    savings = [int(_) for _ in input().split()]
    price = int(input())
    print(get_shopping_day(savings, price, left=0, right=len(savings)), end=' ')
    print(get_shopping_day(savings, price * 2, left=0, right=len(savings)))
