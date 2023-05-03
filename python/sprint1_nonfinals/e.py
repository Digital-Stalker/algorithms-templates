def get_longest_word(line: str) -> str:
    # Здесь реализация вашего решения
    word = ''
    simbols = 0
    for i in line:
        if simbols < len(i):
            simbols -= simbols
            simbols += len(i)
            word = i
    return word


def read_input() -> str:
    _ = input()
    line = input().strip().split()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
