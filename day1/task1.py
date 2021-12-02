import numpy as np


def get_input():
    with open('input.txt') as input_file:
        numbers = input_file.readlines()
    numbers = [int(number.replace('\n', '')) for number in numbers]
    return np.array(numbers)


if __name__ == '__main__':
    depths = get_input()
    delta = depths - np.concatenate([np.array([np.nan]), depths[:-1]])
    print(len(delta[delta > 0]))
