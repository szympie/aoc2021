from functools import reduce

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


def get_basin(arr, point):
    stack = [point]
    visited = []
    basin_values = []
    while stack:
        x, y = stack.pop()
        basin_values.append(arr[x, y])
        if arr[x - 1, y] != 9:
            stack.append((x - 1, y))
        if arr[x + 1, y] != 9:
            stack.append((x + 1, y))
        if arr[x, y - 1] != 9:
            stack.append((x, y - 1))
        if arr[x, y + 1] != 9:
            stack.append((x, y + 1))
        visited.append((x, y))
        stack = list(set(stack).difference(set(visited)))
    return basin_values


if __name__ == '__main__':
    heights = get_input('input.txt')
    shifts = get_shifted(np.pad(heights, 1, constant_values=9))
    diffs = heights - shifts
    minimum_points = np.where(np.all(diffs < 0, axis=0))
    map = np.pad(heights, 1, constant_values=9)
    basins = []
    for x, y in zip(minimum_points[0], minimum_points[1]):
        basin = get_basin(map, (x + 1, y + 1))
        basins.append(basin)
    basins = sorted(basins, key=len, reverse=True)
    largest_sizes = [len(basin) for basin in basins[:3]]
    result = reduce((lambda x, y: x * y), largest_sizes)
    a=1
    print(result)
