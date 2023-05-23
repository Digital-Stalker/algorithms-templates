# 87634595
def calculator_polska(operators: list) -> int:
    stack = []
    for value in operators:
        if value == '+':
            val2 = stack[0]
            val1 = stack[1]
            calc = int(val1) + int(val2)
            stack = [calc] + stack[2:]
        elif value == '-':
            val2 = stack[0]
            val1 = stack[1]
            calc = int(val1) - int(val2)
            stack = [calc] + stack[2:]
        elif value == '*':
            val2 = stack[0]
            val1 = stack[1]
            calc = int(val1) * int(val2)
            stack = [calc] + stack[2:]
        elif value == '/':
            val2 = stack[0]
            val1 = stack[1]
            calc = int(val1) // int(val2)
            stack = [calc] + stack[2:]
        else:
            stack = [value] + stack
    return stack[0]


if __name__ == '__main__':
    expression = input().split()
    print(calculator_polska(expression))
