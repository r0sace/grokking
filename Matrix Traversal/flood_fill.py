def flood_fill(matrix, start_cell, color):
    row = start_cell[0]
    col = start_cell[1]
    value = matrix[row][col]

    if value == color:
        return matrix

    return fill_flood(matrix, row, col, value, color)


def fill_flood(matrix, x, y, value, color):
    if x >= len(matrix) or x < 0:
        return

    if y >= len(matrix[0]) or y < 0:
        return

    if matrix[x][y] != value or matrix[x][y] == color:
        return

    matrix[x][y] = color

    fill_flood(matrix, x + 1, y, value, color)
    fill_flood(matrix, x - 1, y, value, color)
    fill_flood(matrix, x, y + 1, value, color)
    fill_flood(matrix, x, y - 1, value, color)

    return matrix


flood_fill([[0,0,0],[0,0,0]], (1,0), 2)
