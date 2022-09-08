import re

fabric_list = [[0 for _ in range(1000)] for _ in range(1000)]
no_overlap_list = []


def lay_claim(line):
    line_search = re.search(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', line)
    _id = int(line_search[1])
    top = int(line_search[2])
    left = int(line_search[3])
    w = int(line_search[4])
    h = int(line_search[5])
    no_overlap_flag = True
    for r in range(w):
        for c in range(h):
            if item := fabric_list[top + r][left + c]:
                no_overlap_flag = False
                if item != 'X' and item in no_overlap_list:
                    no_overlap_list.remove(fabric_list[top + r][left + c])
                fabric_list[top + r][left + c] = 'X'
            else:
                fabric_list[top + r][left + c] = _id
    if no_overlap_flag:
        no_overlap_list.append(_id)


def count_overlap():
    return sum(fabric_list[r].count('X') for r in range(1000))


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

    # PART 1
    for line in data:
        lay_claim(line)
    print(count_overlap())
    print(no_overlap_list[0])
