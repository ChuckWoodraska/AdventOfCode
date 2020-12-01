# PART1
with open("input.txt", "r") as f:
    num_list = f.read().splitlines()
    print(num_list)
    for n in num_list:
        for n2 in num_list:
            if int(n) + int(n2) == 2020:
                print(int(n), int(n2))
                print(int(n)*int(n2))
                break

# PART2
with open("input.txt", "r") as f:
    num_list = f.read().splitlines()
    print(num_list)
    for n in num_list:
        for n2 in num_list:
            for n3 in num_list:
                if int(n) + int(n2) + int(n3) == 2020:
                    print(int(n), int(n2), int(n3))
                    print(int(n)*int(n2)*int(n3))
                    break