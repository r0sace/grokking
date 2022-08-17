def matrix_cycle(matrix):
    values = set()
    row = len(matrix)
    column = len(matrix[0])

    for i in range(row):
        for j in range(column):
            if matrix[i][j] not in values:
                if cycle_checker(matrix, i, j, (i, j), matrix[i][j]):
                    return True

    return False


def cycle_checker(matrix, x, y, origin, val):
    if x >= len(matrix) or x < 0:
        return 0

    if y >= len(matrix[0]) or y < 0:
        return 0

    if matrix[x][y] == val:
        return 1

    size = 0

    if (x, y) == origin and size > 4:
        return True

    size += cycle_checker(matrix, x + 1, y, origin, val)
    size += cycle_checker(matrix, x - 1, y, origin, val)
    size += cycle_checker(matrix, x, y + 1, origin, val)
    size += cycle_checker(matrix, x, y - 1, origin, val)


matrix_cycle([['a', 'a', 'a', 'a'], ['b', 'a', 'c', 'a'], ['b', 'a', 'c', 'a'], ['b', 'a', 'a', 'a']])
