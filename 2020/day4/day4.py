import re
with open("input.txt", "r") as f:
    lines = f.read()

passports = lines.split("\n\n")

# PART 1
total = 0
for p in passports:
    flags = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0}
    attr_lines = re.split('\n| ', p)
    for l in attr_lines:
        if l.split(':')[0] in flags:
            flags[l.split(':')[0]] += 1
    if all(value > 0 for value in flags.values()):
        total += 1
print(total)


# PART 2

total = 0
for p in passports:
    flags = {'byr': 0, 'iyr': 0, 'eyr': 0, 'hgt': 0, 'hcl': 0, 'ecl': 0, 'pid': 0}
    attr_lines = re.split('\n| ', p)
    for l in attr_lines:
        k, v = l.split(':')
        if k == 'byr':
            try:
                byr = int(v)
                if 2002 >= byr >= 1920:
                    flags[k] += 1
            except:
                pass

        elif k == 'iyr':
            try:
                iyr = int(v)
                if 2020 >= iyr >= 2010:
                    flags[k] += 1
            except:
                pass
        elif k == 'eyr':
            try:
                eyr = int(v)
                if 2030 >= eyr >= 2020:
                    flags[k] += 1
            except:
                pass
        elif k == 'hgt':
            try:
                hgt_type = v[-2:]
                hgt_value = int(v[:-2])
                if (
                    hgt_type == 'cm'
                    and 193 >= hgt_value >= 150
                    or hgt_type != 'cm'
                    and hgt_type == 'in'
                    and 76 >= hgt_value >= 59
                ):
                    flags[k] += 1
            except:
                pass
        elif k == 'hcl':
            if re.match('^#[0-9a-fA-F]{6}', v):
                flags[k] += 1
        elif k == 'ecl':
            if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                flags[k] += 1
        elif k == 'pid':
            if re.match('^[0-9]{9}$', v):
                flags[k] += 1
    if all(value > 0 for value in flags.values()):
        total += 1
print(total)
