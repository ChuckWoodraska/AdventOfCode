from itertools import combinations
with open('input.txt') as f:
    lines = [int(x) for x in f.read().splitlines()]

current_iter = 0
num_list_len = 25
invalid_num = 0
while current_iter+num_list_len != len(lines)-1 or not invalid_num:
    if lines[current_iter+num_list_len+1] not in [x + y for x, y in combinations(lines[current_iter:current_iter+num_list_len+1], 2)]:
        invalid_num = lines[current_iter+num_list_len+1]
    current_iter += 1
print(invalid_num)

index = 0
end_index = lines.index(invalid_num)
stop_flag = 0
while index != end_index or not stop_flag:
    total = 0
    inner_index = index
    while total < invalid_num:
        total += lines[inner_index]
        if total == invalid_num:
            stop_flag = max(lines[index:inner_index]) + min(lines[index:inner_index])
            break
        inner_index += 1
    index += 1
print(stop_flag)
