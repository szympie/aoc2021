import numpy as np
import pandas as pd

def get_input():
    with open('input.txt') as input_file:
        numbers = input_file.readlines()
    numbers = [int(number.replace('\n', '')) for number in numbers]
    return np.array(numbers)


if __name__ == '__main__':
    depths = get_input()
    sliding_sums = pd.Series(depths).rolling(3).sum()
    delta = sliding_sums - np.concatenate([np.array([np.nan]), sliding_sums[:-1]])
    print(len(delta[delta > 0]))

