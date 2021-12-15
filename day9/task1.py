import numpy as np


def get_input(path):
    with open(path, 'r') as input_file:
        lines = input_file.readlines()
    numbers = [list(line.replace('\n', '')) for line in lines]
    numbers = np.array(numbers).astype(int)
    return numbers


def get_shifted(x):
    up = x[0:-2, 1:-1]
    right = x[1:-1, 2:]
    down = x[2:, 1:-1]
    left = x[1:-1, 0:-2]
    return np.stack([up, right, down, left])


if __name__ == '__main__':
    heights = get_input('input.txt')
    shifts = get_shifted(np.pad(heights, 1, constant_values=9))
    diffs = heights - shifts
    minimum_points = (np.all(diffs<0, axis=0))
    minimum_values = heights[minimum_points] + 1
    print(minimum_values.sum())
