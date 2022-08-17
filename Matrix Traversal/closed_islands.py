def closed_islands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]
    island_count = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 1 and not visited[x][y]:
                if explore_island(matrix, visited, x, y):
                    island_count += 1

    return island_count


def explore_island(matrix, visited, x, y):
    if x < 0 or x >= len(matrix):
        return False

    if y < 0 or y >= len(matrix[0]):
        return False

    if matrix[x][y] == 0 or visited[x][y]:
        return True

    visited[x][y] = True
    is_closed = True

    explore_island(matrix, visited, x + 1, y)
    explore_island(matrix, visited, x - 1, y)
    explore_island(matrix, visited, x, y + 1)
    explore_island(matrix, visited, x, y - 1)

    return is_closed


closed_islands([[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, ]])
