from math import ceil

import numpy as np
import pandas as pd


def get_oxygen(lines, sequence=''):
    if len(lines) == 1:
        return sequence + ''.join(str(e) for e in lines[0])
    s = lines[:, 0].sum()
    if s >= (len(lines) / 2):
        sub = lines[lines[:, 0] == 1]
        sub = sub[:, 1:]
        sequence = sequence + '1'
        return get_oxygen(sub, sequence)
    else:
        sub = lines[lines[:, 0] == 0]
        sub = sub[:, 1:]
        sequence = sequence + '0'
        return get_oxygen(sub, sequence)


def get_co2(lines, sequence=''):
    if len(lines) == 1:
        return sequence + ''.join(str(e) for e in lines[0])
    s = lines[:, 0].sum()
    if s >= (len(lines) / 2):
        sub = lines[lines[:, 0] == 0]
        sub = sub[:, 1:]
        sequence = sequence + '0'
        return get_co2(sub, sequence)
    else:
        sub = lines[lines[:, 0] == 1]
        sub = sub[:, 1:]
        sequence = sequence + '1'
        return get_co2(sub, sequence)


def get_input_np(path):
    with open(path, 'r') as input_file:
        lines = [list(line.replace('\n', '')) for line in input_file.readlines()]
    lines = np.array(lines).astype(int)
    return lines




if __name__ == '__main__':
    lines_np = get_input_np('input.txt')
    # lines_np = np.array(temp_array)
    oxygen = get_oxygen(lines_np)
    co2 = get_co2(lines_np)

    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)
    print(oxygen*co2)
