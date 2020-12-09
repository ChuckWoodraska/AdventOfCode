import re

with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = []

for l in lines:
    m = re.match('^([\w]+)\s(\D)(\d+)', l)
    instructions.append([m.group(1), m.group(2), int(m.group(3))])

acc = 0
index = 0
ins_list = []
while True:
    if index in ins_list:
        break
    ins_list.append(index)
    current_instruction = instructions[index]
    print(current_instruction)
    if current_instruction[0] == 'nop':
        index += 1
    elif current_instruction[0] == 'acc':
        if current_instruction[1] == '+':
            acc += current_instruction[2]
        else:
            acc -= current_instruction[2]
        index += 1
    else:
        if current_instruction[1] == '+':
            index += current_instruction[2]
        else:
            index -= current_instruction[2]
    print(acc, index)

print(acc)
# instructions = [re.match('^([\w]+)\s(\D)(\d+)', l) for l in lines]
# print(instructions)

# PART 2
acc = 0
index = 0
ins_list = []
try_list = []
for idx, i in enumerate(instructions):
    if i[0] == 'nop' or i[0] == 'jmp':
        try_list.append(idx)

print(try_list)
import copy

for t in try_list:
    acc = 0
    index = 0
    ins_list = []
    new_instructions = copy.deepcopy(instructions)
    if instructions[t][0] == 'nop':
        new_instructions[t][0] = 'jmp'
    elif instructions[t][0] == 'jmp':
        new_instructions[t][0] = 'nop'
    # print(t)
    # print(new_instructions)
    while True:
        if index in ins_list:
            break
        ins_list.append(index)
        current_instruction = new_instructions[index]
        # print(current_instruction)
        if current_instruction[0] == 'nop':
            index += 1
        elif current_instruction[0] == 'acc':
            if current_instruction[1] == '+':
                acc += current_instruction[2]
            else:
                acc -= current_instruction[2]
            index += 1
        else:
            if current_instruction[1] == '+':
                index += current_instruction[2]
            else:
                index -= current_instruction[2]
        # print(acc, index)

        if index == (len(instructions)):
            print(acc)
            break

# print(acc)
