def check_number(num):
    num = str(num)
    dup_check = False
    ascend_check = True
    for c in range(len(num) - 1):
        if num[c] == num[c + 1]:
            dup_check = True
        elif num[c] > num[c + 1]:
            ascend_check = False
    return bool(dup_check and ascend_check)


def check_number2(num):
    num = str(num)
    dup_check = False
    ascend_check = True
    for c in range(len(num) - 1):
        if num[c] == num[c + 1] and num.count(num[c]) == 2:
            dup_check = True
        elif num[c] > num[c + 1]:
            ascend_check = False
    return bool(dup_check and ascend_check)


def main():
    with open("input.txt", "r") as f:
        start, finish = f.read().split("-")
        total = sum(1 for n in range(int(start), int(finish)) if check_number(n))
        print(total)


def main2():
    with open("input.txt", "r") as f:
        start, finish = f.read().split("-")
        total = sum(1 for n in range(int(start), int(finish)) if check_number2(n))
        print(total)


if __name__ == "__main__":
    main()
