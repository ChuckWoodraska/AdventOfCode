two_three_list = [0, 0]


def check_twos_and_threes(c_dict):
    two = 0
    three = 0
    for k, v in c_dict.items():
        if v == 2 and not two:
            two = 1
        elif v == 3 and not three:
            three = 1
        elif two and three:
            break
    two_three_list[0] += two
    two_three_list[1] += three
    return


with open('input.txt', 'r') as f:
    data = f.read()

    # PART 1
    for line in data.splitlines():
        char_dict = {}
        for c in line:
            if char_dict.get(c):
                char_dict[c] += 1
            else:
                char_dict[c] = 1
        check_twos_and_threes(char_dict)
    print(two_three_list[0] * two_three_list[1])

    # PART 2
    data_dict = {i: {} for i in range(len(data.splitlines()[0]))}
    for line in data.splitlines():
        for i in range(len(line)):
            new_id = line[:i] + line[i+1:]
            if data_dict[i].get(new_id):
                data_dict[i][new_id] += 1
            else:
                data_dict[i][new_id] = 1
    for v in data_dict.values():
        for k2, v2 in v.items():
            if v2 == 2:
                print(k2)
