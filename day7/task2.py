import numpy as np


def get_input(path):
    with open(path, 'r') as positions_file:
        positions = positions_file.readline()
        positions = [int(p) for p in positions.split(',')]
    return positions


def get_compound_cost(x):
    return np.arange(1, x + 1).sum()


if __name__ == '__main__':
    # positions = np.array([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
    positions = get_input('input.txt')
    costs = np.tile(np.ogrid[0:max(positions)].reshape(-1, 1), len(positions))
    costs = np.abs(positions - costs)
    get_compound_cost = np.vectorize(get_compound_cost)
    costs = get_compound_cost(costs).sum(axis=1)

    best_position = np.argmin(costs)
    cost = costs[best_position]
    print(f"Pos: {best_position}, cost: {cost}")
