import numpy as np


def get_input(path):
    with open(path, 'r') as input_file:
        lines = [list(line.replace('\n', '')) for line in input_file.readlines()]
    lines = np.array(lines).astype(int)
    return lines


if __name__ == '__main__':
    lines = get_input('input.txt')
    sums = lines.sum(axis=0)
    most_commons = (sums > len(lines) // 2).astype(int)
    least_commons = (sums < len(lines) // 2).astype(int)

    gamma = int(''.join(most_commons.astype(str)), 2)
    epsilon = int(''.join(least_commons.astype(str)), 2)

    print(gamma * epsilon)
