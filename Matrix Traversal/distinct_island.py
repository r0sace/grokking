def distinct_islands(matrix):
    row = len(matrix)
    col = len(matrix[0])
    traversal_path = set()
    visited = [[False for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                traversal_path.add(explore_island(matrix, i, j, 'O', visited))

    if '' in traversal_path:
        traversal_path.remove('')

    return len(traversal_path)

def explore_island(matrix, x, y, direction, visited):
    if x >= len(matrix) or x < 0:
        return ""

    if y >= len(matrix[0]) or y < 0:
        return ""

    if matrix[x][y] == 0 or visited[x][y] is True:
        return ""

    visited[x][y] = True
    traversal = direction

    traversal += explore_island(matrix, x + 1, y, 'D', visited)
    traversal += explore_island(matrix, x - 1, y, 'U', visited)
    traversal += explore_island(matrix, x, y + 1, 'R', visited)
    traversal += explore_island(matrix, x, y - 1, 'L', visited)

    traversal += 'B'

    return traversal


distinct_islands([[1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1]])
