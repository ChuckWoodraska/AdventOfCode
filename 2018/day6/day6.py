from collections import namedtuple


def manhattan_distance(point_a, centers):
    min_dist = [None, None, False]
    for point_b in centers:
        dist = abs(point_a[0] - point_b.x) + abs(point_a[1] - point_b.y)
        if dist == 0:
            return point_b.id
        if min_dist[0] is None:
            min_dist[0] = dist
            min_dist[1] = point_b.id
        elif dist < min_dist[0]:
            min_dist[0] = dist
            min_dist[1] = point_b.id
            min_dist[2] = False
        elif dist == min_dist[0]:
            min_dist[0] = dist
            min_dist[1] = point_b.id
            min_dist[2] = True
    return '.' if min_dist[2] else min_dist[1]


def manhattan_distance_part2(point_a, centers):
    total_dist = sum(
        abs(point_a[0] - point_b.x) + abs(point_a[1] - point_b.y)
        for point_b in centers
    )

    return '.' if total_dist < 10000 else 0


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

    # Figure out array size
    x_size = max(int(line.split(', ')[0]) for line in data) + 1
    y_size = max(int(line.split(', ')[1]) for line in data) + 1
    grid_list = [[0 for _ in range(y_size)] for _ in range(x_size)]

    coordinate_list = []
    disregard_set = set()
    Point = namedtuple('Point', 'id x y')
    # Load coodinates
    for index, line in enumerate(data):
        new_point = Point(index, *map(int, line.split(', ')))
        coordinate_list.append(new_point)



    # PART 1
    for x in range(len(grid_list)):
        for y in range(len(grid_list[x])):
            grid_list[x][y] = manhattan_distance([x, y], coordinate_list)
            if y in [0, y_size - 1]:
                disregard_set.add(grid_list[x][y])
    disregard_set.update(grid_list[0])
    disregard_set.update(grid_list[x_size - 1])
    disregard_set.remove('.')
    all_id_set = set(list(range(len(coordinate_list))))
    check_set = all_id_set - disregard_set
    max_total = 0
    for item in check_set:
        total = sum(grid_list[s].count(item) for s in range(x_size))
        if total > max_total:
            max_total = total
    print(max_total)

    for x in range(len(grid_list)):
        for y in range(len(grid_list[x])):
            grid_list[x][y] = manhattan_distance_part2([x, y], coordinate_list)
    total = sum(grid.count('.') for grid in grid_list)
    print(total)
