result1 = 0
result2 = 0

with open("input.txt", "r") as file:
    lines = file.readlines()

matrix = [list(line.strip()) for line in lines]
rows = len(matrix)
cols = len(matrix[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# part 1
def search_xmas(i, j, rows, cols) -> int:
    occurences = 0
    xmas = "XMAS"

    if matrix[i][j] == xmas[0]:
        for dir in directions:
            matches = 1
            x, y = i, j
            for letter in xmas[1:]:
                x += dir[0]
                y += dir[1]
                if not (0 <= x < rows) or not (0 <= y < cols):
                    break
                if matrix[x][y] == letter:
                    matches += 1
                else:
                    break
            if matches == 4:
                occurences += 1

    return occurences

# part 2
def search_x_mas(i, j) -> int:
    found_diags = 0

    if (matrix[i][j] == "A"):
        if (matrix[i - 1][j - 1] == "M" and matrix[i + 1][j + 1] == "S"):
            found_diags += 1
        elif (matrix[i - 1][j - 1] == "S" and matrix[i + 1][j + 1] == "M"):
            found_diags += 1

        if (matrix[i + 1][j - 1] == "M" and matrix[i - 1][j + 1] == "S"):
            found_diags += 1
        elif (matrix[i + 1][j - 1] == "S" and matrix[i - 1][j + 1] == "M"):
            found_diags += 1

    if found_diags == 2:
        return 1
    else:
        return 0


for i in range(0, rows):
    for j in range(0, cols):
        result1 += search_xmas(i, j, rows, cols)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        result2 += search_x_mas(i, j)

print(result1)
print(result2)
