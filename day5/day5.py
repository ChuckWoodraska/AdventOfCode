from string import ascii_lowercase


def check_pair(a, b):
    if ord(a) - 32 == ord(b) or ord(a) + 32 == ord(b):
        return True
    return False


def react(polymer):
    buf = []
    for c in polymer:
        if buf and check_pair(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return len(buf)


with open('input.txt', 'r') as f:
    data = f.read().strip()

    # PART 1
    print(react(data))

    # PART 2
    letter_dict = {}
    for l in ascii_lowercase:
        data_replaced = data.replace(l, '').replace(l.upper(), '')
        letter_dict[l] = react(data_replaced)
    print(min(letter_dict.values()))

