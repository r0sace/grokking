def biggest_island(matrix):
    largest_island = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                island_size = explore_island(matrix, i, j)
                largest_island = max(largest_island, island_size)

    return largest_island


def explore_island(matrix, x, y):
    if (x < 0 or x >= len(matrix)) or y < 0 or y >= len(matrix[0]):
        return 0

    if matrix[x][y] == 0:
        return 0

    matrix[x][y] = 0
    size = 1

    size += explore_island(matrix, x + 1, y)
    size += explore_island(matrix, x - 1, y)
    size += explore_island(matrix, x, y + 1)
    size += explore_island(matrix, x, y - 1)

    return size



