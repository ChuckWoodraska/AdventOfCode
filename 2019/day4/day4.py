def check_number(num):
    num = str(num)
    dup_check = False
    ascend_check = True
    for c in range(0, len(num) - 1):
        if num[c] == num[c + 1]:
            dup_check = True
        elif num[c] > num[c + 1]:
            ascend_check = False
    if dup_check and ascend_check:
        return True
    else:
        return False


def check_number2(num):
    num = str(num)
    dup_check = False
    ascend_check = True
    for c in range(0, len(num) - 1):
        if num[c] == num[c + 1] and num.count(num[c]) == 2:
            dup_check = True
        elif num[c] > num[c + 1]:
            ascend_check = False
    if dup_check and ascend_check:
        return True
    else:
        return False


def main():
    with open("input.txt", "r") as f:
        total = 0
        start, finish = f.read().split("-")
        for n in range(int(start), int(finish)):
            if check_number(n):
                total += 1
        print(total)


def main2():
    with open("input.txt", "r") as f:
        total = 0
        start, finish = f.read().split("-")
        for n in range(int(start), int(finish)):
            if check_number2(n):
                total += 1
        print(total)


if __name__ == "__main__":
    main()
