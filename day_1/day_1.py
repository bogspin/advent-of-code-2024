# part 1
result1 = 0
left = []
right = []

with open("input.txt", "r") as file:
    for line in file:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)

for l, r in zip(sorted(left), sorted(right)):
    result1 += abs(l - r)

print(result1)

# part 2
result2 = 0
locations = dict.fromkeys(left)

for location in locations:
    result2 += location * right.count(location)

print(result2)