def trace_wire(wire_dirs):
    last_pos = [0, 0]
    grid_dict = {}
    length = 0
    for direction in wire_dirs:

        way = direction[0]
        amount = int(direction[1:])
        if way == 'R':
            for x in range(1,amount+1):
                grid_pos = f'{last_pos[0] + x}_{last_pos[1]}'
                length += 1
                if grid_pos not in grid_dict:
                    grid_dict[grid_pos] = length
            last_pos[0] += amount
        elif way == 'L':
            for x in range(1,amount+1):
                grid_pos = '{}_{}'.format(last_pos[0]-x, last_pos[1])
                length += 1
                if grid_pos not in grid_dict:
                    grid_dict[grid_pos] = length
            last_pos[0] -= amount
        elif way == 'U':
            for y in range(1,amount+1):
                grid_pos = '{}_{}'.format(last_pos[0], last_pos[1]+y)
                length += 1
                if grid_pos not in grid_dict:
                    grid_dict[grid_pos] = length
            last_pos[1] += amount
        elif way == 'D':
            for y in range(1,amount+1):
                grid_pos = '{}_{}'.format(last_pos[0], last_pos[1]-y)
                length += 1
                if grid_pos not in grid_dict:
                    grid_dict[grid_pos] = length
            last_pos[1] -= amount
    return grid_dict


def main():
    with open('input.txt', 'r') as f:
        first, second = f.read().split('\n')
        first_grid = trace_wire(first.split(','))
        second_grid = trace_wire(second.split(','))
        intersection_grid = set(first_grid.keys()) & set(second_grid.keys())
        # print(intersection_grid)
        part_1 = min(
            abs(int(i.split('_')[0])) + abs(int(i.split('_')[1]))
            for i in intersection_grid
        )

        part_2 = min(second_grid[i] + first_grid[i] for i in intersection_grid)
        print(part_1, part_2)


if __name__ == '__main__':
    main()
