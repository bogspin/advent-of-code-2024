from itertools import product

result1 = 0
result2 = 0

def solve_eq(res, args) -> int:
    op_len = len(args) - 1
    ops = product("+*", repeat=op_len)
    for op in ops:
        result = args[0]
        for arg, operator in zip(args[1:], op):
            if operator == "+":
                result += arg
            if operator == "*":
                result *= arg

        if result == res:
            return res    

    return 0

def solve_part2(res, args) -> int:
    op_len = len(args) - 1
    ops = product("+*|", repeat=op_len)
    for op in ops:
        result = args[0]
        for arg, operator in zip(args[1:], op):
            if operator == "+":
                result += arg
            if operator == "*":
                result *= arg
            if operator == "|":
                 result = int(str(result) + str(arg))

        if result == res:
            return res    

    return 0

with open("input.txt", "r") as file:
    equations = []
    for line in file:
        res, args = line.split(':')
        res = int(res)
        args = [int(arg) for arg in args.split()]
        result1 += solve_eq(res, args)
        result2 += solve_part2(res, args)

print(result1)
print(result2)