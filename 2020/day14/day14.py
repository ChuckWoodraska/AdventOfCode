import re

with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = []

for l in lines:
    print(l)
    m = re.match('^([\w]+)\[*(\d*)\]*\s=\s(\w+)', l)
    print(m.groups())
    print(m[0])
    # if m.group(1) == "mask":
    instructions.append([m[1], m[2], m[3]])
    # elif m.group(1) == "mem":
    #     instructions.append([m.group(1), m.group(2), m.group(3)])
print(instructions)

mask = ''
def run_mask(num):
    print(mask)
    bin_num = bin(num)[2:].zfill(36)
    new_num = []
    for index, c in enumerate(mask):
        if c in ['X', bin_num[index]]:
            new_num.append(bin_num[index])
        else:
            new_num.append(c)
    print(bin(num)[2:].zfill(36))
    return int(''.join(new_num), 2)


mem_slots = {}
for i in instructions:
    if i[0] == 'mask':
        mask = i[2]
    elif i[0] == 'mem':
        mem_slots[i[1]] = run_mask(int(i[2]))
        # mem_slots[mem_slot]

total = 0
for k, v in mem_slots.items():
    print(k, v)
    total += v

print(total)