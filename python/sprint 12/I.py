class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        return self.queue[self.head]

    def size(self):
        if self.is_empty():
            return None
        return self.size


def get_queue(size, commands):
    queue = MyQueueSized(size)
    answer = []
    for com in commands:
        if com.split(' ')[0] == 'push':
            if queue.push(int(com.split(' ')[1])) == 'error':
                answer.append('error')
        elif com == 'pop':
            answer.append(queue.pop())
        elif com == 'peek':
            answer.append(queue.peek())
        elif com == 'size':
            answer.append(queue.size)
    return answer


if __name__ == '__main__':
    count_commands = int(input())
    max_size = int(input())
    command = [input() for _ in range(count_commands)]
    print(*get_queue(max_size, command), sep='\n')
