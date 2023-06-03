def gen_bracket(control, n1, n2, bracket):
    if n1 == 0 and n2 == 0:
        print(bracket)
    else:
        if n1 > 0:
            gen_bracket(control + 1, n1 - 1, n2, bracket + '(')
        if control > 0 and n2 > 0:
            gen_bracket(control - 1, n1, n2 - 1, bracket + ')')


if __name__ == '__main__':
    count = int(input())
    gen_bracket(control=0, n1=count, n2=count, bracket='')
