class Graph:
    def __init__(self):
        self.nodes = dict()
        self.neighbors = dict()

    def add_edge(self, nodes):
        self.add_node(nodes[0])
        self.add_node(nodes[1])
        self.neighbors[nodes[0]].add(nodes[1])
        self.neighbors[nodes[1]].add(nodes[0])

    def add_node(self, node: str):
        if node not in self.nodes:
            type = 'big' if node.isupper() else 'small'
            self.nodes[node] = {'name': node, 'type': type}
            self.neighbors[node] = set()

    def get_unvisited_neighbors(self, node: str, route):
        neighbors = self.neighbors[node]
        neighbors = [n for n in neighbors if n.isupper() or n not in route]
        return neighbors

    def find_all_routes(self, start: str = 'start', end: str = 'end'):
        routes = []
        stack = []
        stack.append([start])
        while len(stack) > 0:
            current_route = stack.pop()
            current_node = current_route[-1]
            if current_node == end:
                routes.append(current_route)
                continue
            unvisited = self.get_unvisited_neighbors(current_node, current_route)
            if len(unvisited) == 0:
                continue
            candidate_routes = [current_route + [n] for n in unvisited]
            stack.extend(candidate_routes)
        return routes


def get_input(path):
    with open(path, 'r') as input_file:
        lines = [line.replace('\n', '').split('-') for line in input_file.readlines()]
    graph = Graph()
    for line in lines:
        graph.add_edge(line)
    return graph


if __name__ == '__main__':
    caves = get_input('input.txt')
    routes = caves.find_all_routes()
    print(len(routes))
