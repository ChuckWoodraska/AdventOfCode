def fuel(line):
    return line // 3 - 2


def main():
    total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            total += fuel(int(line))
    print(total)


def main2():
    total2 = 0
    with open('input.txt', 'r') as f:
        for line in f:
            temp = fuel(int(line))
            while temp > 0:
                total2 += temp
                temp = fuel(int(temp))

    print(total2)


if __name__ == '__main__':
    main2()