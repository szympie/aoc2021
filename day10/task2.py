import numpy as np

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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


def find_completion(line):
    stack = []
    for idx, character in enumerate(line):
        if character in ['[', '(', '<', '{']:
            stack.append(character)
        elif character in [']', ')', '>', '}']:
            if stack[-1] == opening_chars[character]:
                stack.pop()
    completion = [closing_chars[char] for char in reversed(stack)]
    return completion


if __name__ == '__main__':
    lines = get_input('input.txt')
    errors = [find_error(line) for line in lines]
    incomplete = [line for line, error in zip(lines, errors) if error is None]
    completions = [find_completion(line) for line in incomplete]
    scores = []
    for completion in completions:
        score = 0
        for character in completion:
            score = score * 5 + points[character]
        scores.append(score)
    scores = np.array(scores)
    print(np.median((scores)))
