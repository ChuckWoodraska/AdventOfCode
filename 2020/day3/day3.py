from functools import reduce
import operator

with open("input.txt", "r") as f:
    row_list = f.read().splitlines()
    total_trees_list = []
    row_len = len(row_list[0])
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for slope in slopes:
        current_row = 0
        current_col = 0
        total_trees = 0

        while current_row + 1 != len(row_list):
            current_col += slope[0]
            current_col = current_col % row_len
            current_row += slope[1]
            if row_list[current_row][current_col] == '#':
                total_trees += 1
        total_trees_list.append(total_trees)
        # print(slope[0], slope[1], total_trees)
    print(total_trees_list, reduce(operator.mul, total_trees_list))
