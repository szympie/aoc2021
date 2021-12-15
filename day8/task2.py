import numpy as np

MAPPING = {
    0: {'a', 'b', 'c', 'e', 'f', 'g'},
    1: {'c', 'f'},
    2: {'a', 'c', 'd', 'e', 'g'},
    3: {'a', 'c', 'd', 'f', 'g'},
    4: {'b', 'c', 'd', 'f'},
    5: {'a', 'b', 'd', 'f', 'g'},
    6: {'a', 'b', 'd', 'e', 'f', 'g'},
    7: {'a', 'c', 'f'},
    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    9: {'a', 'b', 'c', 'd', 'f', 'g'},
}
COUNTS = {k: len(v) for k, v in MAPPING.items()}


def get_input(path):
    with open(path) as patterns_file:
        lines = patterns_file.readlines()
    patterns, outputs = [], []
    for line in lines:
        p, o = line.replace('\n', '').split(' | ')
        patterns.append([set(el) for el in p.split(' ')])
        outputs.append([set(el) for el in o.split(' ')])
    return patterns, outputs


def get_lengths(array):
    return [len(x) for x in array]


def find_mapping(pattern):
    map = {}
    map[1] = [p for p in pattern if len(p) == 2]
    assert len(map[1]) == 1
    map[1] = map[1][0]
    map[7] = [p for p in pattern if len(p) == 3]
    assert len(map[7]) == 1
    map[7] = map[7][0]
    map[4] = [p for p in pattern if len(p) == 4]
    assert len(map[4]) == 1
    map[4] = map[4][0]
    map[8] = [p for p in pattern if len(p) == 7]
    assert len(map[8]) == 1
    map[8] = map[8][0]
    map[3] = [p for p in pattern if len(p) == 5 and map[7].issubset(p)]
    assert len(map[3]) == 1
    map[3] = map[3][0]
    map[2] = [p for p in pattern if
              len(p) == 5 and map[8].difference(map[4]).difference(map[7]).issubset(p)]
    assert len(map[2]) == 1
    map[2] = map[2][0]

    map[5] = \
        [p for p in pattern if
         len(p) == 5 and p != map[3] and p != map[2]]
    assert len(map[5]) == 1
    map[5] = map[5][0]

    map[9] = [p for p in pattern if len(p) == 6 and map[4].issubset(p)]
    assert len(map[9]) == 1
    map[9] = map[9][0]
    map[6] = \
        [p for p in pattern if
         len(p) == 6 and map[5].difference(map[1]).issubset(p) and p != map[9]]
    assert len(map[6]) == 1
    map[6] = map[6][0]
    map[0] = [p for p in pattern if len(p) == 6 and p != map[6] and p != map[9]]
    assert len(map[0]) == 1
    map[0] = map[0][0]
    return map


if __name__ == '__main__':
    patterns, outputs = get_input('input.txt')
    decoded_outputs = []
    for pattern, output in zip(patterns, outputs):
        mapping = find_mapping(pattern)
        output_string = ''
        for o in output:
            x = list(mapping.keys())[list(mapping.values()).index(o)]
            output_string += str(x)
        decoded_outputs.append(int(output_string))
    print(decoded_outputs)
    print(sum(decoded_outputs))
