import numpy as np
import pandas as pd


def get_input(path):
    with open(path, 'r') as lines_file:
        lines = lines_file.readlines()
        lines = [line.replace(' -> ', ',').replace('\n', '') for line in lines]
        lines = [line.split(',') for line in lines]
    return np.array(lines).astype(int)


def clean_straight_line(start, stop):
    x0 = min(start[0], stop[0])
    x1 = max(start[0], stop[0])
    y0 = min(start[1], stop[1])
    y1 = max(start[1], stop[1])
    return x0, x1, y0, y1


if __name__ == '__main__':
    lines = get_input('input.txt')
    starts = lines[:, :2]
    stops = lines[:, 2:]

    map = np.zeros((1000, 1000))
    for start, stop in zip(starts, stops):
        x0, x1, y0, y1 = clean_straight_line(start, stop)
        if start[0] == stop[0]:
            map[x0, y0:y1 + 1] += 1
        elif start[1] == stop[1]:
            map[x0:x1 + 1, y0] += 1
        elif (start-stop)[0] > 0 and(start-stop)[1] <0 :
            diag = np.rot90(np.diag(np.ones(y1-y0+1)))
            map[x0:x1+1, y0:y1+1] += diag
            a=1
        elif (start - stop)[0] < 0 and (start - stop)[1] < 0:
            diag = np.diag(np.ones(y1 - y0 + 1))
            map[x0:x1 + 1, y0:y1 + 1] += diag
        elif (start-stop)[0] > 0 and (start-stop)[1]>0:
            diag = np.diag(np.ones(y1 - y0+1))
            map[x0:x1+1, y0:y1+1] += diag
            a=1
        elif (start-stop)[0] < 0 and (start-stop)[1]>0:
            diag = np.rot90(np.diag(np.ones(y1 - y0+1)))
            map[x0:x1+1, y0:y1+1] += diag
            a=1

    print(len(map[map>1]))
