import numpy as np


def get_input(path):
    with open(path, 'r') as bingo_file:
        numbers_to_choose = bingo_file.readline()
        numbers_to_choose = [int(number) for number in numbers_to_choose.split(',')]
        lines = bingo_file.readlines()
    lines = [line.replace('\n', '').split(' ') for line in lines if line != '\n']
    no_boards = len(lines) // 5
    boards = [[int(number) for number in line if number != ''] for line in lines]
    boards = np.array(boards).reshape((no_boards, 5, 5))
    return numbers_to_choose, boards


if __name__ == '__main__':
    numbers_to_choose, boards = get_input('input.txt')
    hits = np.zeros_like(boards)
    for number in numbers_to_choose:
        hits[boards == number] = 1
        rows_hits = hits.sum(axis=2)
        column_hits = hits.sum(axis=1)
        if 5 in rows_hits or 5 in column_hits:
            winner_board = int(np.where(rows_hits == 5)[0])
            number_sum = boards[winner_board][hits[winner_board] == 0].sum()
            print(number_sum * number)
            break

