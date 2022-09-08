def count_meta(node, total):
    child_nodes = node.pop(0)
    meta_nodes = node.pop(0)
    for _ in range(child_nodes):
        total = count_meta(node, total)
    for _ in range(meta_nodes):
        total += node.pop(0)
    return total

def count_meta2(node, total, lookup, _id):
    child_nodes = node.pop(0)
    meta_nodes = node.pop(0)
    for child in range(1, child_nodes+1):
        lookup[child] = count_meta2(node, total, {}, child)
    mid_total = 0
    if child_nodes:
        for _ in range(meta_nodes):
            meta_index = node.pop(0)
            mid_total += lookup.get(meta_index, 0)
    else:
        for _ in range(meta_nodes):
            meta_index = node.pop(0)
            mid_total += meta_index
    return mid_total

with open('input.txt', 'r') as f:
    data = f.read().split()
    temp_data = list(map(int, data))
    # PART 1
    print(count_meta(temp_data, 0))

    # PART 2
    temp_data = list(map(int, data))
    lookup_dict = count_meta2(temp_data, 0, {}, 0)
    print(lookup_dict)

