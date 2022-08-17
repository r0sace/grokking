
def island_perimeter(matrix):
    row = len(matrix)
    col = len(matrix[0])
    visited = [[False for i in range(col)] for j in range(row)]

    for x in range(row):
        for y in range(col):
            if matrix[x][y] == 1:
                return get_perimeter(matrix, x, y, visited)


def get_perimeter(matrix, x, y, visited):
    if x >= len(matrix) or x < 0:
        return 1

    if y >= len(matrix[0]) or y < 0:
        return 1

    if matrix[x][y] == 0:
        return 1

    if visited[x][y] is True:
        return 0


    visited[x][y] = True
    size = 0

    size += get_perimeter(matrix, x+ 1, y, visited)
    size += get_perimeter(matrix, x - 1, y, visited)
    size += get_perimeter(matrix, x, y + 1, visited)
    size += get_perimeter(matrix, x, y - 1, visited)

    return size


island_perimeter([[1,0]])