with open("input.txt", "r") as f:
    password_list = f.read().splitlines()
    total = 0
    p2_total = 0
    for password in password_list:
        minmax, character, tmp_pass = password.split(" ")
        mi, ma = minmax.split("-")
        mi = int(mi)
        ma = int(ma)
        character = character[0]
        char_count = tmp_pass.count(character)
        # PART 1
        if mi <= char_count <= ma:
            total += 1
        # PART 2
        if (tmp_pass[mi-1] == character) ^ (tmp_pass[ma-1] == character):
            p2_total += 1
    print(total)
    print(p2_total)
