import pandas as pd

grid_list = [[0 for y in range(301)] for x in
             range(301)]

grid_dict = {}

def calculate_power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level = power_level * rack_id
    hundreds = (power_level // 100) % 10
    return hundreds - 5


with open('input.txt', 'r') as f:
    data = int(f.read().splitlines()[0])

    for x in range(1, 301):
        for y in range(1, 301):
            grid_list[y][x] = calculate_power_level(x, y, data)
            grid_dict['{}{}'.format(y, x)] = calculate_power_level(x, y, data)
    max_power = [0, 0, 0]
    for size in range(3, 301):
        print(size)
        for x in range(1, 301-size):
            for y in range(1, 300-size):
                total = 0
                for i in range(size):
                    for j in range(size):
                        total += grid_dict['{}{}'.format(y+i, x+j)]
                        # total += grid_list[y+i][x+j]
                if total > max_power[0]:
                    max_power[0] = total
                    max_power[1] = (x, y)
                    max_power[2] = size
    print(max_power)
    # grid_list[33][45] = '********'
    # df = pd.DataFrame(grid_list)
    # print(df.loc[30:50, 30:50])