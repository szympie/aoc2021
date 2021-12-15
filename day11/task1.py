import numpy as np


def get_input(path):
    with open(path, 'r') as input_file:
        lines = [line.replace('\n', '') for line in input_file.readlines()]
    numbers = np.array([[int(char) for char in line] for line in lines])
    return numbers


def run_step(energy_arr):
    energy_arr += np.ones_like(energy_arr)
    energy_arr = np.pad(energy_arr, 1)
    flashed = np.zeros_like(energy_arr)
    flashes_count = 0
    while 1:
        flashes = np.zeros_like(energy_arr)
        flashes[energy_arr > 9] = 1
        flashes[flashed >= 1] = 0
        if np.any(flashes > 0):
            flash_points = np.where(flashes)
            flashes_burst = np.zeros_like(energy_arr)
            for x, y in zip(flash_points[0], flash_points[1]):
                flashes_count +=1
                flashes_burst[x - 1:x + 2, y - 1:y + 2] += 1
            energy_arr += flashes_burst
            flashed[flashes > 0] = 1
        else:
            break
    energy_arr = energy_arr[1:-1, 1:-1]
    flashed = flashed[1:-1, 1:-1]
    energy_arr[flashed > 0] = 0
    return energy_arr, flashes_count


if __name__ == '__main__':
    energy_arr = get_input('test_input.txt')
    flashes_count = 0
    for step in range(100):
        energy_arr, flashes = run_step(energy_arr)
        flashes_count += flashes
    print(flashes_count)
