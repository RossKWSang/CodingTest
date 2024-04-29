"""
A turn-based strategy game has a grid with water and land.
The grid contains a True value where it's water and False where it's land.

The player controls a boat unit with a particular movement pattern.
It can only move to fixed destinations from its current position as shown in th image below
"""


game_matrix = [
    [False, True, True, False, False, False],
    [True, True, True, False, False, False],
    [True, True, True, True, True, True],
    [False, True, True, False, True, True],
    [False, True, True, True, False, True],
    [False, False, False, False, False, False]
]


def can_travel_to(position, initial_x, initial_y, destination_x, destination_y):
    movement = [[2, 0], [-1, 0], [0, 1], [0, -1]]
    boarder_limit = len(position)
    visited = [[False] * boarder_limit] * boarder_limit

    def dfs(x, y):
        # group_count
        visited[x][y] = True

        for move in movement:
            new_x = x + move[0]
            new_y = y + move[1]

            if new_x < 0 or new_y < 0 or new_x >= boarder_limit or new_y >= boarder_limit:
                continue

            if not position[new_x][new_y]:
                continue

            if visited[new_x][new_y]:
                continue

            dfs(new_x, new_y)

    dfs(initial_x, initial_y)

    if destination_x < 0 or destination_y < 0 or destination_x >= boarder_limit or destination_y >= boarder_limit:
        return False

    return visited[destination_x][destination_y]


print(can_travel_to(game_matrix, 3, 2, 2, 2))
print(can_travel_to(game_matrix, 3, 2, 3, 4))
print(can_travel_to(game_matrix, 3, 2, 6, 2))
