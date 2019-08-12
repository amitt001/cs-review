"""Given a graph check if it is m colourable


Check if the graph is 3 colourable.

(3)---(2)
 |   / |
 |  /  |
 | /   |
(0)---(1)

Input:
graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
i = 3

Output: True

- Iterate and store neighbor color and used colors till now.

Time: O(n^2), Space: O(n)
"""


class Vertex:
    def __init__(self, color):
        self.color = color


def m_colourable(graph, m):
    color_set = set()
    color_counter = 0
    vertex_map = {}

    # e: vertex
    for v, neighbors in enumerate(graph):
        tmp_color_set = color_set.copy()
        for nv, n in enumerate(neighbors):
            if n == 0:
                continue
            if v == nv:
                continue

            if nv in vertex_map:
                vert = vertex_map[nv]
                tmp_color_set.discard(vert.color)

        if len(tmp_color_set) == 0:
            color_counter += 1
            tmp_color_set.add(color_counter)
            color_set.add(color_counter)
        vertex_map[v] = Vertex(list(tmp_color_set)[0])
    return color_counter == m


if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    assert m_colourable(graph, 3) is True
    assert m_colourable(graph, 2) is False
