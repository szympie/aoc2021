import numpy as np

MAPPING = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'],
    1: ['c', 'f'],
    2: ['a', 'c', 'd', 'e', 'g'],
    3: ['a', 'c', 'd', 'f', 'g'],
    4: ['b', 'c', 'd', 'f', ],
    5: ['a', 'b', 'd', 'f', 'g'],
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f', ],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g'],
}
COUNTS = {k: len(v) for k, v in MAPPING.items()}


def get_input(path):
    with open(path) as patterns_file:
        lines = patterns_file.readlines()
    patterns, outputs = [], []
    for line in lines:
        p, o = line.replace('\n', '').split(' | ')
        patterns.append(p.split(' '))
        outputs.append(o.split(' '))
    return patterns, outputs


def get_lengths(array):
    return [len(x) for x in array]


if __name__ == '__main__':
    patterns, outputs = get_input('input.txt')
    outputs_lengths = np.array([get_lengths(x) for x in outputs])

    counts = {key: len(outputs_lengths[outputs_lengths == COUNTS[key]]) for key in COUNTS}

    print(counts[1]+counts[4]+counts[7]+counts[8])

