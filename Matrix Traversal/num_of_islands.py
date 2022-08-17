def num_of_islands(matrix):
    total_islands = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                total_islands += 1
                visit_island(matrix, i, j)

    return total_islands


def visit_island(matrix, x, y):
    if (x < 0 or x >= len(matrix)) or y < 0 or y >= len(matrix[0]):
        return

    if matrix[x][y] == '0':
        return

    matrix[x][y] = '0'

    visit_island(matrix, x + 1, y)
    visit_island(matrix, x - 1, y)
    visit_island(matrix, x, y + 1)
    visit_island(matrix, x, y - 1)


num_of_islands(["1"])
