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
    triplets = {k: [k[0] + v, v + k[1]] for k, v in rules.items()}
    counts = {rule: 0 for rule in rules}
    sings_frequencies = {v: 0 for k, v in rules.items()}
    for pair in get_pairs(template):
        counts[pair] += 1
    for char in template:
        sings_frequencies[char] += 1
    for step in range(steps):
        new_counts = {rule: 0 for rule in rules}
        for pair, count in counts.items():
            if count > 0:
                new_pairs = triplets[pair]
                new_counts[new_pairs[0]] += count
                new_counts[new_pairs[1]] += count
                sings_frequencies[rules[pair]] += count
            counts = new_counts.copy()
    return sings_frequencies


if __name__ == '__main__':
    template, rules = get_input('input.txt')

    voc = polymerize(template, rules, 40)
    counts = [v for k, v in voc.items()]
    print(max(counts) - min(counts))
