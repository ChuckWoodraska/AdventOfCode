with open("input.txt", "r") as f:
    lines = f.read().splitlines()

m = 0
for line in lines:
    row = sum([2 ** i for i, x in enumerate(line[0:7][::-1]) if x == "B"])
    seat = sum([2 ** i for i, x in enumerate(line[7:10][::-1]) if x == "R"])
    m = max(row * 8 + seat, m)
print(m)

seats = set()
for line in lines:
    row = sum([2 ** i for i, x in enumerate(line[0:7][::-1]) if x == "B"])
    seat = sum([2 ** i for i, x in enumerate(line[7:10][::-1]) if x == "R"])
    seatid = row * 8 + seat
    seats.add(seatid)

for i in range(max(seats)):
    if i not in seats and i + 1 in seats and i - 2 in seats:
        print(i)
