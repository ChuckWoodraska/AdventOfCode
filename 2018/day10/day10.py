import re


class Star:
    def __init__(self, x, y, dx, dy):
        # print(x, y, dx, dy)
        self.x = int(x)
        self.y = int(y)
        self.dx = int(dx)
        self.dy = int(dy)

    def step(self):
        self.x += self.dx
        self.y += self.dy

    def __repr__(self):
        return f'x={self.x} y={self.y}'


stars = []


def make_grid(grid_min, s):
    min_x = min(stars, key=lambda star: star.x).x
    max_x = max(stars, key=lambda star: star.x).x
    min_y = min(stars, key=lambda star: star.y).y
    max_y = max(stars, key=lambda star: star.y).y
    # print(min_x, max_x, min_y, max_y)
    if s == 10144:
        star_list = [['.' for _ in range(max_y + 1)] for _ in range(max_x + 1)]
        for star in stars:
            star_list[star.x][star.y] = '#'
        for row in range(len(star_list) - 1, 0, -1):
            print(star_list[row][100:])
        print(min_x, max_x, min_y, max_y)
    temp_min = abs(min_x - max_x) * abs(min_y - max_y)
    # print(temp_min)
    if temp_min < grid_min[0]:
        grid_min[0] = temp_min
        grid_min[1] = s
    return grid_min


with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    for line in data:
        stars.append(
            Star(*re.match('position=<\s*(-?\d*),\s*(-?\d*)>\s*velocity=<\s*(-?\d*),\s*(-?\d*)>', line).groups()))
    grid_min = [10000000000, 0]
    for s in range(10200):
        grid_min = make_grid(grid_min, s)
        for star in stars:
            star.step()

    print(grid_min)
