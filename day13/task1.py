import numpy as np


def get_input(path):
    with open(path, 'r') as input_file:
        lines = input_file.readlines()
        lines = [line.replace('\n', '') for line in lines]
        lines = [line for line in lines if line != '']
    folds = [line for line in lines if line.startswith('fold')]
    folds = [fold.replace('fold along ','') for fold in folds]
    folds = [(fold.split('=')[0],int(fold.split('=')[1])) for fold in folds]
    dots = [line for line in lines if not line.startswith('fold')]
    dots = [[int(coord) for coord in line.split(',')] for line in dots]
    return dots, folds


def dots_to_array(dots):
    dots = np.array(dots)
    array_size = (max(dots[:, 1] + 1), max(dots[:, 0] + 1))
    array = np.zeros(array_size)
    for dot in dots:
        array[dot[1], dot[0]] = 1
    return array


def fold_paper(paper, fold):
    axis = 1 if fold[0] == 'x' else 0
    fold_num = fold[1]
    if axis == 0:
        first_half = paper[:fold_num, :]
        second_half = np.flip(paper[fold_num + 1:, :], axis)
    if axis == 1:
        first_half = paper[:, :fold_num]
        second_half = np.flip(paper[:, fold_num + 1:], axis)
    paper = first_half + second_half
    return paper


if __name__ == '__main__':
    dots, folds = get_input('input.txt')
    paper = dots_to_array(dots)
    for fold in folds:
        paper = fold_paper(paper, fold)
    paper[paper>1]=1
    a=1

