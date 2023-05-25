# 87672793
class Deque:
    def __init__(self, elem):
        self.max_elem = elem
        self.__dec = [None] * elem
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def push_back(self, value):
        if self.__size != self.max_elem:
            self.__dec[self.__head - 1] = value
            self.__head = (self.__head - 1) % self.max_elem
            self.__size += 1
        else:
            raise IndexError

    def push_front(self, value):
        if self.__size != self.max_elem:
            self.__dec[self.__tail] = value
            self.__tail = (self.__tail + 1) % self.max_elem
            self.__size += 1
        else:
            raise IndexError

    def pop_front(self):
        if self.__size != 0:
            pop_elem = self.__dec[self.__tail - 1]
            self.__dec[self.__tail - 1] = None
            self.__tail = (self.__tail - 1) % self.max_elem
            self.__size -= 1
            return pop_elem
        else:
            raise IndexError

    def pop_back(self):
        if self.__size != 0:
            pop_elem = self.__dec[self.__head]
            self.__dec[self.__head] = None
            self.__head = (self.__head + 1) % self.max_elem
            self.__size -= 1
            return pop_elem
        else:
            raise IndexError


def get_dec(size, commands):
    dec = Deque(size)
    answer = []
    for _com in commands:
        comm, *args = _com.split()
        if comm == 'push_back':
            try:
                dec.push_back(int(*args))
            except IndexError:
                answer.append('error')
        elif comm == 'push_front':
            try:
                dec.push_front(int(*args))
            except IndexError:
                answer.append('error')
        elif comm == 'pop_front':
            try:
                answer.append(dec.pop_front())
            except IndexError:
                answer.append('error')
        elif comm == 'pop_back':
            try:
                answer.append(dec.pop_back())
            except IndexError:
                answer.append('error')
    return answer


if __name__ == '__main__':
    count_commands = int(input())
    max_size = int(input())
    command = [input() for _ in range(count_commands)]
    print(*get_dec(max_size, command), sep='\n')
