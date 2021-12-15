points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

opening_chars = {
    ')': '(',
    ']': '[',
    '>': '<',
    '}': '{',
}
closing_chars = {
    '(': ')',
    '[': ']',
    '<': '>',
    '{': '}',
}


def get_input(path):
    with open(path, 'r') as input_file:
        lines = input_file.readlines()
    return [line.replace('\n', '') for line in lines]


def find_error(line):
    stack = []
    for idx, character in enumerate(line):
        if character in ['[', '(', '<', '{']:
            stack.append(character)
        elif character in [']', ')', '>', '}']:
            if stack[-1] == opening_chars[character]:
                stack.pop()
            else:
                return {'expected': closing_chars[stack[-1]],
                        'found': character}


if __name__ == '__main__':
    lines = get_input('test_input.txt')
    errors = [find_error(line) for line in lines]
    score = 0
    for error in errors:
        if error:
            score += points[error['found']]
    print(score)
