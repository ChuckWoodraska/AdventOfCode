from functools import reduce

with open("input.txt", "r") as f:
    groups = f.read().split('\n\n')

print(sum(map(lambda x: len(set(list(x.replace('\n', '')))), groups)))
print(sum(map(lambda x: len(reduce(lambda a, b: set(list(a)).intersection(set(list(b))), x.split('\n'))), groups)))
