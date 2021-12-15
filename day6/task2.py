import math
import numpy as np


def get_input(path):
    with open(path, 'r') as input_file:
        counts = input_file.readline()
    counts = [int(count) for count in counts.split(',')]
    return counts


def get_fish_offspring(days, offspring):
    if days - 8 < 0:
        return offspring
    else:
        new_offspring = offspring + math.floor((days - 8) / 6) + 1
        return get_fish_offspring(days - 8, new_offspring)


if __name__ == '__main__':
    counts = np.array(get_input('input.txt'))
    # counts = np.array([3, 4, 3, 1, 2])
    lookup = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for key in lookup:
        lookup[key] += len(counts[counts == key])
    for day in range(256):
        new_lookup = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for key, count in reversed(lookup.items()):
            if key > 0:
                new_lookup[key - 1] += count
            else:
                new_lookup[8] += count
                new_lookup[6] += count
            lookup = new_lookup.copy()
        counts = [count for _, count in lookup.items()]
        print(counts)
    counts = sum([count for _, count in lookup.items()])
    print(counts)
