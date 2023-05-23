# 87600872
class Dec:
    def __init__(self, elem):
        self.max_elem = elem
        self.dec = [None] * elem
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, value):
        if self.size != self.max_elem:
            self.dec[self.head - 1] = value
            self.head = (self.head - 1) % self.max_elem
            self.size += 1
        else:
            return 'error'

    def push_front(self, value):
        if self.size != self.max_elem:
            self.dec[self.tail] = value
            self.tail = (self.tail + 1) % self.max_elem
            self.size += 1
        else:
            return 'error'

    def pop_front(self):
        if self.size == 0:
            return 'error'
        pop_elem = self.dec[self.tail - 1]
        self.dec[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_elem
        self.size -= 1
        return pop_elem

    def pop_back(self):
        if self.size == 0:
            return 'error'
        pop_elem = self.dec[self.head]
        self.dec[self.head] = None
        self.head = (self.head + 1) % self.max_elem
        self.size -= 1
        return pop_elem


def get_dec(size, commands):
    dec = Dec(size)
    answer = []
    for com in commands:
        if com.split(' ')[0] == 'push_back':
            if dec.push_back(int(com.split(' ')[1])) == 'error':
                answer.append('error')
        elif com.split(' ')[0] == 'push_front':
            if dec.push_front(int(com.split(' ')[1])) == 'error':
                answer.append('error')
        elif com == 'pop_front':
            answer.append(dec.pop_front())
        elif com == 'pop_back':
            answer.append(dec.pop_back())
    return answer


if __name__ == '__main__':
    count_commands = int(input())
    max_size = int(input())
    command = [input() for _ in range(count_commands)]
    print(*get_dec(max_size, command), sep='\n')
