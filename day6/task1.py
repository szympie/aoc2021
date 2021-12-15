class Starfish:
    def __init__(self, days: int):
        self.days = days

    def __repr__(self):
        return str(self.days)

    def reproduce(self):
        if self.days == 0:
            self.days = 6
            return [self, Starfish(8)]
        else:
            self.days -= 1
            return [self]


def get_input(path):
    with open(path, 'r') as input_file:
        counts = input_file.readline()
    counts = [int(count) for count in counts.split(',')]
    return counts


def run_simulation(counts, days):
    starfishes = [Starfish(count) for count in counts]
    for day in range(days):
        new_generation = []
        for starfish in starfishes:
            new_generation.extend(starfish.reproduce())
        starfishes = new_generation
    return starfishes


if __name__ == '__main__':
    # counts = get_input('input.txt')
    counts = [8]
    final_gen = run_simulation(counts, 35)
    print(len(final_gen))


