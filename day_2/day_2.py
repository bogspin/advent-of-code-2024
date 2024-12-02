# part 1
result1 = 0
result2 = 0

def isSafe(level: list) -> bool:
    if (sorted(level) != level and sorted(level, reverse=True) != level):
        return False

    idx = 0
    while (idx < len(level) - 1):
        if (abs(level[idx] - level[idx + 1]) > 3 or level[idx] == level[idx + 1]):
            return False
        idx += 1

    return True

with open("input.txt", "r") as file:
    for line in file:
        level = list(map(int, line.split()))
        result1 += isSafe(level=level)

        # brute force part 2
        for i in range(len(level)):
            if isSafe(level[:i] + level[i + 1:]):
                result2 += 1
                break

print(result1)
print(result2)
