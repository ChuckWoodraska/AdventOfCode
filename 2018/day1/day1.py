# PART 1
with open('input.txt', 'r') as f:
    data = f.read()
    total = sum(int(line) for line in data.splitlines())
    print(total)

# PART 2
    freq_set = set()
    total = 0
    not_found = True
    while not_found:
        for line in data.splitlines():
            freq_set.add(total)
            total += int(line)
            if total in freq_set:
                print(total)
                not_found = False
                break
