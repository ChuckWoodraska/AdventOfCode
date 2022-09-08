with open('input.txt') as f:
    lines = [int(x) for x in f.read().splitlines()]
    lines.sort()
    lines.insert(0, 0)
    lines.append(max(lines)+3)

# PART 1
diff_list = []

index = 0
while index != len(lines)-1:
    diff_list.append(lines[index+1]-lines[index])
    index += 1
print(diff_list.count(1)*diff_list.count(3))

# PART 2
unique_combos = 1
index = 0
temp_list = []
while index != len(lines)-1:
    next_num = lines[index] + 1
    if next_num in lines:
        temp_list.append(lines[index])
    else:
        if len(temp_list) > 1:
            unique_combos = unique_combos * (pow(2, len(temp_list) - 1) - max((len(temp_list) - 3), 0))
        temp_list = []
    index += 1
print(unique_combos)