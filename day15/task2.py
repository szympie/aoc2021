import networkx
import numpy as np
from networkx import DiGraph


class MapGraph:
    def __init__(self, array):
        self.graph = DiGraph()
        self.i_max = array.shape[0]
        self.j_max = array.shape[1]
        self.nodes = {f'{i}-{j}': array[i, j] for i in range(self.i_max) for j in range(self.j_max)}
        self.edges = {f'{i}-{j}': self.get_neighbors(i, j) for i in range(self.i_max) for j in
                      range(self.j_max)}
        for node in self.nodes:
            self.graph.add_node(node)
        for edge, neighbors in self.edges.items():
            for n in neighbors:
                self.graph.add_edge(edge, n, weight=self.nodes[n])

    def get_neighbors(self, i, j):
        neighbors = []
        if i > 0:
            neighbors.append(f'{i - 1}-{j}')
        if i < self.i_max - 1:
            neighbors.append(f'{i + 1}-{j}')
        if j > 0:
            neighbors.append(f'{i}-{j - 1}')
        if j < self.j_max - 1:
            neighbors.append(f'{i}-{j + 1}')
        return neighbors


def get_input(path):
    with open(path, 'r') as input_file:
        lines = [list(line.replace('\n', '')) for line in input_file.readlines()]
    cave_map = np.array(lines).astype(int)
    org_map = cave_map.copy()
    for x in range(1, 5):
        cave_map = np.concatenate([cave_map, org_map + x], axis=0)
        cave_map[cave_map >= 10] = np.mod(cave_map[cave_map >= 10], 10) + 1
    org_map = cave_map.copy()
    for x in range(1, 5):
        cave_map = np.concatenate([cave_map, org_map + x], axis=1)
        cave_map[cave_map >= 10] = np.mod(cave_map[cave_map >= 10], 10) + 1
    return cave_map


if __name__ == '__main__':
    cave_map = get_input('input.txt')
    graph = MapGraph(cave_map)
    shortest_path = networkx.shortest_path(graph.graph, '0-0',
                                           f'{graph.i_max - 1}-{graph.i_max - 1}', 'weight')
    distance = 0
    for node in shortest_path[1:]:
        distance += graph.nodes[node]
    print(distance)
