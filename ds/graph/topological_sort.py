# DFS with cycle check
from typing import List
from graph import directed_graph


# Using a recursion stack
def dag_dfs(start, adj_list, visited, rec_stack, result):
    """Also checks for a cycle and returns False is cycle found"""

    visited.add(start)
    rec_stack.add(start)
    for v in adj_list.get(start, []):
        if v.key not in visited:
            if dag_dfs(v.key, adj_list, visited, rec_stack, result) is False:
                return False
        elif v.key in rec_stack:
            return False

    rec_stack.discard(start)
    if start not in result:
        # FIFO for DFS
        result.insert(0, start)
    return True


def dfs(nums: int, adj_list: dict) -> list:
    visited = set()
    rec_stack = set()
    result = []
    # O(v+e)
    for u in range(nums):
        # Not already visited
        if u not in visited:
            if dag_dfs(u, adj_list, rec_stack, visited, result) is False:
                return []
    return result


if __name__ == '__main__':
    adj_list = directed_graph(
        [
            [5, 2],
            [5, 0],
            [4, 0],
            [4, 1],
            [2, 3],
            [3, 1]
        ]
    )

    print(dfs(6, adj_list))
