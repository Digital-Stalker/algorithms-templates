# 87695963
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def calculator_polska(operators: list):
    stack = Stack()
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b
    }
    for value in operators:
        if value in operations:
            val1, val2 = stack.pop(), stack.pop()
            stack.push(operations[value](val2, val1))
        else:
            stack.push(int(value))
    return stack.pop()


if __name__ == '__main__':
    expression = input().split()
    print(calculator_polska(expression))
