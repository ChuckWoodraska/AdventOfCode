# PART 1
with open("input.txt", "r") as f:
    num_list = [int(x) for x in f.read().splitlines()]
    print(num_list)
    total = 0
    n1 = num_list.pop(0)
    for n2 in num_list:
        if n1 < n2:
            total += 1
        n1 = n2
print(total)

# PART 2
with open("input.txt", "r") as f:
    num_list = [int(x) for x in f.read().splitlines()]
    print(num_list)
    total = 0
    n1 = num_list.pop(0)
    n2 = num_list.pop(0)
    n3 = num_list.pop(0)
    for n4 in num_list:
        if (n1+n2+n3) < (n2+n3+n4):
            total += 1
        n1, n2, n3 = n2, n3, n4
print(total)