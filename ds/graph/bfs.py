from graph import directed_graph


def bfs(start, adj_list):
    bfs_q = [start]
    visited = set(bfs_q)
    result = []
    while bfs_q:
        u = bfs_q.pop(0)
        # if u in visited:
        #     continue
        for v in adj_list.get(u, []):
            if v.key not in visited:
                bfs_q.append(v.key)
                visited.add(v.key)
        result.append(u)
    return result

if __name__ == '__main__':
    adj_list = directed_graph(
        [
            [0, 1],
            [0, 2],
            [0, 5],
            [1, 3],
            [2, 5],
            [3, 5]
        ]
    )

    print(bfs(0, adj_list))
