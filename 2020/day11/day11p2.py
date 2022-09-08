import copy

with open('input.txt') as f:
    lines = list(f.read().splitlines())

print(lines)

change_flag = True

adjacent_checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

new_lines = copy.deepcopy(lines)
def check_empty(r, c):
    empty_flag = True
    for x in adjacent_checks:
        i, j = x[0], x[1]
        while lines[]
        if len(lines)-1 >= r + x[0] >= 0 and len(lines[0])-1 >= c + x[1] >= 0:
            if lines[r+x[0]][c+x[1]] == '#':
                empty_flag = False
                break
    return empty_flag

def check_crowded(r, c):
    filled = sum(
        len(lines) - 1 >= r + x[0] >= 0
        and len(lines[0]) - 1 >= c + x[1] >= 0
        and lines[r + x[0]][c + x[1]] == '#'
        for x in adjacent_checks
    )

    return filled >= 5

while True:
    print(new_lines)
    for r in range(len(lines)):
        new_row = []
        for c in range(len(lines[0])):
            if (
                lines[r][c] == 'L'
                and check_empty(r, c)
                or lines[r][c] != 'L'
                and lines[r][c] == '#'
                and not check_crowded(r, c)
            ):
                new_row.append('#')
            elif (
                lines[r][c] == 'L'
                and not check_empty(r, c)
                or lines[r][c] != 'L'
                and lines[r][c] == '#'
                and check_crowded(r, c)
            ):
                new_row.append('L')
            else:
                new_row.append(lines[r][c])
        new_lines[r] = ''.join(new_row)
    if lines == new_lines:
        break
    lines = copy.deepcopy(new_lines)

print(lines)
print(sum(x.count('#') for x in lines))
