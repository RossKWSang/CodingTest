map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
]


def route_exist(start_x, start_y, end_x, end_y, map):
    map_boarder = len(map_matrix)
    visited = [[False for _ in range(map_boarder)] for _ in range(map_boarder)]
    visited[start_x][start_y] = True
    movement = [[1, 0], [0, 1]]

    def dfs(x, y):
        visited[x][y] = True
        for move in movement:
            new_x = x + move[0]
            new_y = y + move[1]

            if new_x >= map_boarder or new_y >= map_boarder:
                continue

            if not map[new_x][new_y]:
                continue

            dfs(new_x, new_y)

    dfs(start_x, start_y)

    return visited[end_x][end_y]


print(route_exist(0, 0, 2, 2, map_matrix))
