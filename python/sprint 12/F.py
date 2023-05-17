class StackMax:
    def __init__(self):
        self.items = []
        self.g_max = []

    def push(self, item):
        if len(self.items) == 0 or item >= self.g_max[-1]:
            self.g_max.append(item)
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return 'error'
        if self.items.pop() == self.g_max[-1]:
            self.g_max.pop()

    def get_max(self):
        if len(self.items) == 0:
            return 'None'
        return self.g_max[-1]


def get_stack(commands):
    stack = StackMax()
    answer = []
    for com in commands:
        if com.split(' ')[0] == 'push':
            stack.push(int(com.split(' ')[1]))
        elif com == 'pop':
            if stack.pop() == 'error':
                answer.append('error')
        elif com == 'get_max':
            answer.append(stack.get_max())
    return answer


if __name__ == '__main__':
    count_commands = int(input())
    command = [input() for _ in range(count_commands)]
    print(*get_stack(command), sep='\n')
