# PART 1
with open("input.txt", "r") as f:
    crab_list = [int(x) for x in f.read().split(',')]
    crab_max = max(crab_list)
    crab_min = min(crab_list)
    fuel_min = 100000000
    for position in range(crab_min, crab_max+1):
        fuel_total = 0
        print(position)
        print(fuel_min)
        for crab in crab_list:
            if fuel_total >= fuel_min:
                break
            while crab != position:
                if crab > position:
                    crab -= 1
                    fuel_total += 1
                else:
                    crab += 1
                    fuel_total += 1
                if fuel_total >= fuel_min:
                    break
        if fuel_total < fuel_min:
            fuel_min = fuel_total
print(fuel_min)

# PART 2
with open("input.txt", "r") as f:
    crab_list = [int(x) for x in f.read().split(',')]
    crab_max = max(crab_list)
    crab_min = min(crab_list)
    fuel_min = 10000000000
    for position in range(crab_min, crab_max+1):
        fuel_total = 0
        print(position)
        print(fuel_min)
        for crab in crab_list:
            if fuel_total >= fuel_min:
                break
            counter = 1
            while crab != position:
                if crab > position:
                    crab -= 1
                    fuel_total += counter
                else:
                    crab += 1
                    fuel_total += counter
                if fuel_total >= fuel_min:
                    break
                counter += 1
        if fuel_total < fuel_min:
            fuel_min = fuel_total
print(fuel_min)


