class NodeQueue:
    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.append(item)
        return self.queue[-1]

    def get(self):
        if self.size() == 0:
            return 'error'
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)


def get_stack(commands):
    stack = NodeQueue()
    answer = []
    for com in commands:
        if com.split(' ')[0] == 'put':
            stack.put(int(com.split(' ')[1]))
        elif com == 'get':
            answer.append(stack.get())
        elif com == 'size':
            answer.append(stack.size())
    return answer


if __name__ == '__main__':
    count_commands = int(input())
    command = [input() for _ in range(count_commands)]
    print(*get_stack(command), sep='\n')
