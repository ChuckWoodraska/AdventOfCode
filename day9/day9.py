import re
from itertools import cycle
from collections import deque, defaultdict


def play_game(players, last_marble):
    player_iter = cycle(range(int(players)))
    player_score = defaultdict(int)
    circle = deque([0])
    current_player = 0
    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            player_score[current_player] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
        current_player = next(player_iter)
    return max(player_score.values())


def main():
    with open('input.txt', 'r') as f:
        data = f.read()
        players, last_marble = re.match('(\d+)\D*(\d+)', data).groups()
        players = int(players)
        # PART 1
        last_marble = int(last_marble)
        print(play_game(players, last_marble))
        # PART 2
        last_marble = int(last_marble) * 100
        print(play_game(players, last_marble))


if __name__ == '__main__':
    main()
