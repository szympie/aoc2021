def get_input(path):
    with open(path, 'r') as input_file:
        lines = input_file.readlines()
        lines = [line.replace('\n', '') for line in lines]
        lines = [line for line in lines if line != '']
    template = lines[0]
    rules = [rule.split(' -> ') for rule in lines[1:]]
    rules = {rule[0]: rule[1] for rule in rules}
    return template, rules


def get_pairs(s: str):
    pairs = [s[idx:idx + 2] for idx in range(len(s) - 1)]
    return pairs


def polymerize(template, rules, steps):
    vocabulary = {}
    to_transform = []
    temp = []
    for c in template:
        if not c in vocabulary:
            vocabulary[c] = 0
        vocabulary[c] += 1
    to_transform.extend(get_pairs(template))
    for step in range(steps):
        for pair in to_transform:
            if pair in rules:
                new_letter = rules[pair]
                if not new_letter in vocabulary:
                    vocabulary[new_letter] = 0
                vocabulary[new_letter] += 1
                temp.append(pair[0] + new_letter)
                temp.append(new_letter + pair[1])
        to_transform = temp.copy()
        temp = []
    return vocabulary


if __name__ == '__main__':
    template, rules = get_input('input.txt')

    voc = polymerize(template, rules, 10)
    counts = [v for k, v in voc.items()]
    print(max(counts) - min(counts))
