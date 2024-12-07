# part 1
result1 = 0

with open("input.txt", "r") as file:
    lines = file.readlines()

matrix = [list(line.strip()) for line in lines]
rows = len(matrix)
cols = len(matrix[0])

for i in range(0, rows):
    for j in range(0, cols):
        if matrix[i][j] == "^":
            starting_pos = (i, j)

i, j = starting_pos
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = (-1, 0)
dir_change = 0
orig_path = []
while 0 <= i < rows and 0 <= j < cols:
    if matrix[i + dir[0]][j + dir[1]] == "#":
        dir_change += 1
        dir = directions[dir_change % 4]

    if matrix[i][j] != "X":
        orig_path.append((i, j))
        matrix[i][j] = "X"
        result1 += 1
    i += dir[0]
    j += dir[1]

print(result1)

# part 2
result2 = 0

for obstacle in orig_path:
    i, j = starting_pos
    dir = (-1, 0)
    dir_change = 0
    path = []

    while 0 <= i < rows and 0 <= j < cols:
        pos = (i, j)
        path.append((pos, dir))
        try:
            while matrix[i + dir[0]][j + dir[1]] == "#" or (i + dir[0], j + dir[1]) == obstacle:
                dir_change += 1
                dir = directions[dir_change % 4]
        except:
            break

        i += dir[0]
        j += dir[1]

        if ((i, j), dir) in path:
            result2 += 1
            break

print(result2)