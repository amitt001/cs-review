"""DFS with check for cycle and visisted node using coloring

WHITE: Not visted
GREY: Visited
BLACK: part of recursion stack
"""
from graph import directed_graph


class Color:
    WHITE = 'WHITE'
    GREY = 'GREY'
    BLACK = 'BLACK'


def dfs_util(start, adj_list, color, result):
    color[start] = Color.BLACK
    for v in adj_list.get(start, []):
        if color[v.key] == Color.WHITE:
            if dfs_util(v.key, adj_list, color, result) is False:
                return False
        elif color[v.key] == Color.BLACK:
            return False

    color[start] = Color.GREY
    if start not in result:
        result.insert(0, start)
    return True


def dfs(nums, adj_list):
    result = []
    color = {u: Color.WHITE for u in range(nums)}
    for u in range(nums):
        if color[u] == Color.WHITE:
            if dfs_util(u, adj_list, color, result) is False:
                return []
    return result


if __name__ == '__main__':
    adj_list = directed_graph(
        [
            [0, 1],
            [1, 3],
            [1, 2],
            [2, 4],
            [0, 4],
        ]
    )

    print(dfs(5, adj_list))
