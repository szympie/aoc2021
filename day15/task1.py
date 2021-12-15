import numpy as np


class Graph:
    def __init__(self, array):
        self.i_max = array.shape[0]
        self.j_max = array.shape[1]
        self.nodes = {f'{i}-{j}': array[i, j] for i in range(self.i_max) for j in range(self.j_max)}
        self.edges = {f'{i}-{j}': self.get_neighbors(i, j) for i in range(self.i_max) for j in
                      range(self.j_max)}

    def get_neighbors(self, i, j):
        neighbors = []
        if i > 0:
            neighbors.append(f'{i - 1}-{j}')
        if i < self.i_max:
            neighbors.append(f'{i + 1}-{j}')
        if j > 0:
            neighbors.append(f'{i}-{j - 1}')
        if j < self.j_max:
            neighbors.append(f'{i}-{j + 1}')
        return neighbors


def dijkstra(graph, start='0-0'):
    unvisited = {node: None for node in graph.nodes}
    visited = {}
    current = start
    current_distance = 0
    unvisited[current] = current_distance
    while 1:
        for neighbor in graph.edges[current]:
            if neighbor not in unvisited:
                continue
            new_distance = current_distance + graph.nodes[neighbor]
            if unvisited[neighbor] is None or unvisited[neighbor] > new_distance:
                unvisited[neighbor] = new_distance
        visited[current] = current_distance
        unvisited.pop(current)
        if len(unvisited) == 0:
            break
        candidates = [(node, distance) for node, distance in unvisited.items() if distance]
        current, current_distance = sorted(candidates, key=lambda x: x[1])[0]
    return visited


def get_input(path):
    with open(path, 'r') as input_file:
        lines = [list(line.replace('\n', '')) for line in input_file.readlines()]
    cave_map = np.array(lines).astype(int)
    return cave_map


if __name__ == '__main__':
    cave_map = get_input('test_2.txt')
    graph = Graph(cave_map)
    x = dijkstra(graph)
    print(x[f'{graph.i_max-1}-{graph.i_max-1}'])
