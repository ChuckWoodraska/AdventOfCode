import math
# PART 1
with open("input.txt", "r") as f:
    byte_list = [x for x in f.read().splitlines()]
    b_list = [0 for x in range(len(byte_list[0]))]
    final = ''
    for byte in byte_list:
        for index,b in enumerate(byte):
            b_list[index] += int(b)
    for b in b_list:
        if int(b) > int(len(byte_list)/2):
            final += '1'
        else:
            final += '0'
    gr = int(final, 2)
    er = ''
    for c in final:
        if c == '1':
            er += '0'
        else:
            er += '1'
    er = int(er, 2)
print(gr*er)

# # PART 2
with open("input.txt", "r") as f:
    byte_list = [x for x in f.read().splitlines()]
    new_list = byte_list
    for index in range(len(byte_list[0])):
        temp_list = []
        b_list = [0 for x in range(len(byte_list[0]))]
        f = ''
        for byte in new_list:
            for i, b in enumerate(byte):
                b_list[i] += int(b)
        for b in b_list:
            if int(b) >= int(math.ceil(len(new_list) / 2)):
                f += '1'
            else:
                f += '0'
        for x in new_list:
            if x[index] == f[index]:
                temp_list.append(x)
        b_list = [0 for x in range(len(new_list[0]))]
        new_list = temp_list
    ogr = int(new_list[0], 2)

    new_list = byte_list
    for index in range(len(byte_list[0])):
        temp_list = []
        b_list = [0 for x in range(len(byte_list[0]))]
        f = ''
        for byte in new_list:
            for i, b in enumerate(byte):
                b_list[i] += int(b)
        for b in b_list:
            if int(b) >= int(math.ceil(len(new_list) / 2)):
                f += '0'
            else:
                f += '1'

        for x in new_list:
            if x[index] == f[index]:
                temp_list.append(x)

        b_list = [0 for x in range(len(new_list[0]))]
        new_list = temp_list
        if len(new_list) == 1:
            break
    csr = int(new_list[0], 2)
print(ogr*csr)
