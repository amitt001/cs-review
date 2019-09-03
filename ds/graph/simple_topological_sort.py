"""Simple stack based topological sort

O(V+E)
"""


class Graph:

    def __init__(self, num_vert):
        self.graph = {}
        self.num_vert = num_vert

    def addEdge(self, u, v):
        if self.graph.get(u) is None:
            self.graph[u] = []
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited.add(v)

        for u in self.graph.get(v, []):
            if u not in visited:
                self.topological_sort_util(u, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        visited = set()
        stack = []

        for i in range(self.num_vert):
            if i not in visited:
                self.topological_sort_util(i, visited, stack)

        return stack


if __name__ == '__main__':
    graph = Graph(6)
    graph.addEdge(5, 0)
    graph.addEdge(5, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 1)
    graph.addEdge(4, 1)
    graph.addEdge(4, 0)
    print(graph.topological_sort())
