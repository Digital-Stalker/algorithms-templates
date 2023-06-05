# 87963333
# Работает, но код стал больше (っ °Д °;)っ
import random
from dataclasses import dataclass


@dataclass
class Student:
    __slots__ = ['name', 'tasks', 'penalty']
    name: str
    tasks: int
    penalty: int

    def __lt__(self, other):
        return (-self.tasks, self.penalty, self.name) < (
            -other.tasks, other.penalty, other.name)

    def __str__(self):
        return self.name


def effective_quicksort(users, low, high):
    if low >= high:
        return -1
    left, right = low, high
    pivot = users[random.randint(low, high)]

    while left <= right:
        while users[left] < pivot:
            left += 1
        while users[right] > pivot:
            right -= 1
        if left <= right:
            users[left], users[right] = users[right], users[left]
            left += 1
            right -= 1
    effective_quicksort(users, low=low, high=right)
    effective_quicksort(users, low=left, high=high)


if __name__ == '__main__':
    number = int(input())
    competitors = []
    for _ in range(number):
        name, tasks, penalty = input().split()
        competitors.append(Student(name, int(tasks), int(penalty)))
    effective_quicksort(competitors, low=0, high=number-1)
    print(*competitors, sep="\n")
