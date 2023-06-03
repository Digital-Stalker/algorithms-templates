def get_bubble_sort(sort_list, num):
    flag = 1
    for j in range(num - 1):
        for i in range(0, num - 1 - j):
            if sort_list[i] > sort_list[i + 1]:
                sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
                flag = 1
        if flag == 1:
            print(' '.join(map(str, sort_list)))
            flag = 0


if __name__ == '__main__':
    cont_sort = int(input())
    elements = [int(_) for _ in input().split()]
    get_bubble_sort(elements, cont_sort)
