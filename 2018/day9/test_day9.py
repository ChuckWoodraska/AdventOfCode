from day9 import play_game


def test_case_1():
    assert play_game(10, 25) == 32


def test_case_2():
    assert play_game(10, 1618) == 8317


def test_case_3():
    assert play_game(13, 7999) == 146373


def test_case_4():
    assert play_game(17, 1104) == 2764


def test_case_5():
    assert play_game(21, 6111) == 54718


def test_case_6():
    assert play_game(30, 5807) == 37305
