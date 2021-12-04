def check_columns(board):
    for c in range(5):
        if [list(r.values())[c] for r in board].count(True) == 5:
            return True
    return False


def check_rows(board):
    for row in board:
        if list(row.values()).count(True) == 5:
            return True
    return False


def check_board(board):
    return check_columns(board) or check_rows(board)


def get_score(num, board):
    return sum([int(k) for row in board for k, v in row.items() if v is False]) * int(num)


def mark_number(num, board):
    for row in board:
        if num in row.keys():
            row[num] = True


def main():
    with open("input.txt", "r") as f:
        all_boards = []
        data = [line.strip() for line in f.readlines()]
        numbers = [x for x in data.pop(0).split(",")]
        data.pop(0)
        board = []
        board_win_track = []
        count = 0
        for line in data:
            if line.strip() != "":
                count += 1
                board.append({x.strip(): False for x in line.split(" ") if x.strip()})
            if count == 5:
                all_boards.append(board)
                board_win_track.append(0)
                board = []
                count = 0
        break_loop = False
        found_first = False
        for n in numbers:
            for b_num, board in enumerate(all_boards):
                mark_number(n, board)
                if check_board(board):
                    if not board_win_track[b_num]:
                        board_win_track[b_num] = get_score(n, board)
                    if board_win_track.count(0) == 0:
                        print(get_score(n, board))
                        break_loop = True
                        break
                    # PART 1
                    if not found_first:
                        print(get_score(n, board))
                        found_first = True
            if break_loop:
                break


if __name__ == '__main__':
    main()