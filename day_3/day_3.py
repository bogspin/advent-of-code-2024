import re

# part 1
result1 = 0
result2 = 0

with open("input.txt", "r") as file:
    instructions = file.read()

valid_instructions = re.findall("mul\((\d+),(\d+)\)", instructions)
for match in valid_instructions:
    result1 += int(match[0]) * int(match[1])

print(result1)

# part 2
dont_list = []
do_list = re.split("(?<!\w)(do|don't)(?!\w)", instructions)

dont_list = [
    do_list[i + 1] for i in range(len(do_list) - 1) if do_list[i] == "don't"
]
for text in dont_list:
    do_list.remove(text)

for text in do_list:
    valid_instructions = re.findall("mul\((\d+),(\d+)\)", text)
    for match in valid_instructions:
        result2 += int(match[0]) * int(match[1])

print(result2)
