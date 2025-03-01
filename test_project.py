import pytest
from project import PlayerH, play_tictactoe, createVals, make_move, is_empty, check_winner

def test_createVals():
    assert createVals() == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def test_make_move():
    game = createVals()
    assert make_move(game, 0, 'X') == True
    assert game[0] == 'X'
    assert make_move(game, 0, 'X') == False

def test_is_empty():
    assert is_empty([" ", " "]) == True
    assert is_empty(["2", "3"]) == False
    assert is_empty(["a", " "]) == True

def test_check_winner():
    game = createVals()
    game[0] = "X"
    game[1] = "X"
    game[2] = "X"

    assert check_winner(game, 2, "X") == True

def test_play_tictactoe_col_win(monkeypatch):
    responses = iter(['0', '1', '3', '5', '6'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    player_1 = PlayerH('X')
    player_2 = PlayerH('O')
    assert play_tictactoe(player_1, player_2) == "X WINNER"

# 0, 1, 3, 5, 6 "X wins"

def test_play_tictactoe_row_win(monkeypatch):
    responses = iter(['0', '8', '1', '5', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    player_1 = PlayerH('X')
    player_2 = PlayerH('O')
    assert play_tictactoe(player_1, player_2) == "X WINNER"

    responses = iter(['8', '0', '7', '1', '3', '2'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    # player_1 = PlayerH('X')
    # player_2 = PlayerH('O')
    assert play_tictactoe(player_1, player_2) == "O WINNER"


def test_play_tictactoe_diagonal_win(monkeypatch):
    responses = iter(['0', '1', '4', '5', '8'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    player_1 = PlayerH('X')
    player_2 = PlayerH('O')
    assert play_tictactoe(player_1, player_2) == "X WINNER"

def test_tie(monkeypatch):
    responses = iter(['0', '1', '3', '4', '7', '6', '2', '5', '8'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    player_1 = PlayerH('X')
    player_2 = PlayerH('O')
    assert play_tictactoe(player_1, player_2) == "TIE GAME"

    # X O X
    # X O O
    # O X X

# def test_invalid_input(monkeypatch):
#     responses = iter(['0', 'bum', '3', '4', '7', '6', '2', '5', '8'])
#     monkeypatch.setattr('builtins.input', lambda _: next(responses))

#     x_player = PlayerH('X')
#     s_player = PlayerH('O')
#     t = TicTacToe()

#     with pytest.raises(ValueError):
#         assert play_game(t, x_player, s_player)
