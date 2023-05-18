def is_correct_bracket_seq(sequence: str) -> bool:
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []
    for char in sequence:
        if char in brackets:
            stack.append(char)
        else:
            if not stack:
                return False
            last = stack.pop()
            if char != brackets[last]:
                return False
    return not stack


if __name__ == '__main__':
    bracket = str(input())
    print(is_correct_bracket_seq(bracket))
