def subsequence(s1, s2) -> bool:
    position = -1
    for i in s1:
        position = s2.find(i, position + 1)
        if position == - 1:
            return False
    return True


if __name__ == '__main__':
    stroka1 = str(input())
    stroka2 = str(input())
    print(subsequence(stroka1, stroka2))
