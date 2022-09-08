import math
# PART 1
with open("input.txt", "r") as f:
    byte_list = list(f.read().splitlines())
    b_list = [0 for _ in range(len(byte_list[0]))]
    for byte in byte_list:
        for index,b in enumerate(byte):
            b_list[index] += int(b)
    final = ''.join('1' if int(b) > len(byte_list) // 2 else '0' for b in b_list)
    gr = int(final, 2)
    er = ''.join('0' if c == '1' else '1' for c in final)
    er = int(er, 2)
print(gr*er)

# # PART 2
with open("input.txt", "r") as f:
    byte_list = list(f.read().splitlines())
    new_list = byte_list
    for index in range(len(byte_list[0])):
        b_list = [0 for _ in range(len(byte_list[0]))]
        for byte in new_list:
            for i, b in enumerate(byte):
                b_list[i] += int(b)
        f = ''.join(
            '1' if int(b) >= int(math.ceil(len(new_list) / 2)) else '0'
            for b in b_list
        )

        temp_list = [x for x in new_list if x[index] == f[index]]
        b_list = [0 for _ in range(len(new_list[0]))]
        new_list = temp_list
    ogr = int(new_list[0], 2)

    new_list = byte_list
    for index in range(len(byte_list[0])):
        b_list = [0 for _ in range(len(byte_list[0]))]
        for byte in new_list:
            for i, b in enumerate(byte):
                b_list[i] += int(b)
        f = ''.join(
            '0' if int(b) >= int(math.ceil(len(new_list) / 2)) else '1'
            for b in b_list
        )

        temp_list = [x for x in new_list if x[index] == f[index]]
        b_list = [0 for _ in range(len(new_list[0]))]
        new_list = temp_list
        if len(new_list) == 1:
            break
    csr = int(new_list[0], 2)
print(ogr*csr)
