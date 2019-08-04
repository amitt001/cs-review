"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""


class Vertext:
    def __init__(self, key):
        self.key = key


def directed_graph(inp):
    """inp = [[u, v], [u1, v1],...]"""
    adj_list = {}
    for u, v in inp:
        adj_list.setdefault(u, []).append(Vertext(v))
    return adj_list


class Color:
    WHITE = 'Not visited'
    GREY = 'Part of recursion stack'
    BLACK = 'Visited'


def dfs_util(start, adj_list, color, element, result):
    if start == element:
        result.insert(0, start)
        return

    color[start] = Color.GREY

    for v in adj_list.get(start, []):
        # Result found, stop the dfs
        if result:
            break
        elif color.get(v.key, Color.WHITE) == Color.WHITE:
            dfs_util(v.key, adj_list, color, element, result)
        elif color.get(v.key, Color.WHITE) == Color.GREY:
            return

    color[start] = Color.BLACK
    # Result found, that means start is a parent of element
    if result:
        result.insert(0, start)


def find_route(x, adj_list):
    # check base cases
    # {
    #     0 -> [1, 2]
    #     1 -> [3],
    #     2 -> [3]
    #     3 -> [4]
    # }
    color = {u: Color.WHITE for u in adj_list}
    result = []

    for u in adj_list:
        if result:
            break
        if color.get(u, Color.WHITE) == Color.WHITE:
            dfs_util(u, adj_list, color, x, result)

    return result


if __name__ == '__main__':
    inp = [[0, 1], [1, 3], [2, 3], [0, 2], [3, 4]]
    element = 4
    adj_list = directed_graph(inp)
    print(find_route(element, adj_list))
