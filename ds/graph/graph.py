from typing import List, Union


class Node:
    def __init__(self, key):
        self.key = key

def directed_graph(data: List[Union[str, str]]) -> dict:
    graph = {}
    for u, v in data:
        node = Node(v)
        graph.setdefault(u, []).append(node)
    return graph

