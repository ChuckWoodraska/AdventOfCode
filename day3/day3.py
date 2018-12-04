import re

fabric_list = [[0 for y in range(1000)] for x in range(1000)]
no_overlap_list = []


def lay_claim(line):
    line_search = re.search(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', line)
    _id = int(line_search.group(1))
    top = int(line_search.group(2))
    left = int(line_search.group(3))
    w = int(line_search.group(4))
    h = int(line_search.group(5))
    no_overlap_flag = True
    for r in range(w):
        for c in range(h):
            item = fabric_list[top + r][left + c]
            if item:
                no_overlap_flag = False
                if item != 'X' and item in no_overlap_list:
                    no_overlap_list.remove(fabric_list[top + r][left + c])
                fabric_list[top + r][left + c] = 'X'
            else:
                fabric_list[top + r][left + c] = _id
    if no_overlap_flag:
        no_overlap_list.append(_id)


def count_overlap():
    total = 0
    for r in range(1000):
        total += fabric_list[r].count('X')
    return total


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

    # PART 1
    for line in data:
        lay_claim(line)
    print(count_overlap())
    print(no_overlap_list[0])
