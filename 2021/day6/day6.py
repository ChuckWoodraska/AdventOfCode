# PART 1
with open("input.txt", "r") as f:
    fish_list = [int(x) for x in f.read().split(',')]
    counter = 0
    while counter < 80:
        new_fish = fish_list
        for index, f in enumerate(fish_list):
            f -= 1
            if f == -1:
                new_fish.append(9)
                new_fish[index] = 6
            else:
                new_fish[index] = f
        fish_list = new_fish
        counter += 1
print(len(fish_list))

# PART 2
with open("input.txt", "r") as f:
    fish_list = [int(x) for x in f.read().split(',')]
    fish_dict = {x: 0 for x in range(9)}
    for fish in fish_list:
        fish_dict[fish] += 1

    for gen in range(256):
        new_fish = fish_dict[0]
        fish_dict[7] += fish_dict[0]
        for interval in range(1, 9):
            fish_dict[interval - 1] = fish_dict[interval]
        fish_dict[8] = new_fish

    print(sum(fish_dict.values()))


