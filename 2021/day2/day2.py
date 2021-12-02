
# PART 1
with open("input.txt", "r") as f:
    instruction_list = [x.split(' ') for x in f.read().splitlines()]
    print(instruction_list)
    h, d = 0, 0
    for instruction in instruction_list:
        if instruction[0] == 'forward':
            h += int(instruction[1])
        elif instruction[0] == 'down':
            d += int(instruction[1])
        elif instruction[0] == 'up':
            d -= int(instruction[1])
print(h*d)

# PART 2
with open("input.txt", "r") as f:
    instruction_list = [x.split(' ') for x in f.read().splitlines()]
    print(instruction_list)
    h, d, a = 0, 0, 0
    for instruction in instruction_list:
        if instruction[0] == 'forward':
            h += int(instruction[1])
            d += int(instruction[1]) * a
        elif instruction[0] == 'down':
            a += int(instruction[1])
        elif instruction[0] == 'up':
            a -= int(instruction[1])
print(h*d)
