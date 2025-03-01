import random
import time
import math

class Player:
    def __init__(self, char):
        self.char = char

    def get_move(self, game):
        pass

class PlayerC(Player):
    def __init__(self, char):
        super().__init__(char)

    def get_move(self, game):
        """
        Computer will choose a random square on the board to move to
        """

        square = random.choice(moves_left(game))
        return square

class PlayerH(Player):
    def __init__(self, char):
        super().__init__(char)

    def get_move(self, game):
        """
        Gets the move from the user, if user gives an invalid option, it will
        continuously ask until given a valid option
        """
        value = None
        while True:
            # Check to see if input user given is a valid answer or open space.
            try:
                value = int(input(f"Player '{self.char}', please enter your move (0-8): "))
                if (value not in moves_left(game)):
                    raise ValueError

                return value

            except ValueError:
                # Ask the user again if they did not give a valid answer
                print('Invalid square. Try again')

def createVals():
    game_board_vals = []
    for _ in range(9):
            game_board_vals.append(' ')
    
    return game_board_vals

def is_empty(game_board):
    """
    Determines if there are any empty squares left
    """
    return ' ' in game_board

def board(game_board):
    print(' ---' + ' --- ' + '---')

    holder = []
    for index in range(3):
        holder.append(game_board[index * 3:(index + 1) * 3])

    for row in holder:
        print('| ' + ' | '.join(row) + ' |')
        print(' ---' + ' --- ' + '---')

def board_outline():
    """
    Will map the corresponding number in the Tic-Tac-Toe grid, to help
    users select the correct move/position when playing
    """
    number_board = []
    temp_list = []
    print(' ---' + ' --- ' + '---')

    for index in range(3):
        temp_list = []
        for jdex in range(index * 3, (index + 1) * 3):
            temp_list.append(str(jdex))
        number_board.append(temp_list)

    for row in number_board:
        print('| ' + ' | '.join(row) + ' |')
        print(' ---' + ' --- ' + '---')

    print('')

def moves_left(game_board):
    """
    Check to see if there are any remanining moves
    """
    moves = []
    for (i, spot) in enumerate(game_board):
        if (spot == ' '):
            moves.append(i)

    return moves

def make_move(game_board, square, char):
    """
    If move is valid, then move to the assigned square with the
    following letter and return 'True'. However, if given an incorrect move
    function will return false.
    """

    if (game_board[square] == ' '):
        game_board[square] = char

        return True

    return False

def check_winner(game_board, square, char):
    """
    Determines the winner if a user has gotten 3 in a row from any direction.
    """

    # Checking for matches in diagonals
    if (square % 2 == 0):
        # top left to bottom right line
        diag1 = [game_board[i] for i in [0, 4, 8]]
        if (all([spot == char for spot in diag1])):
            return True

        # top right to bottom left line
        diag2 = [game_board[i] for i in [2, 4, 6]]
        if all([spot == char for spot in diag2]):
            return True

    # Checking for matches in rows
    r_index = math.floor(square / 3)
    row = game_board[r_index * 3 : (r_index + 1) * 3]
    if (all(spot == char for spot in row)):
        return True

    # Checking for matches in columns
    c_index = square % 3
    column = [game_board[c_index + i * 3] for i in range(3)]
    if (all([spot == char for spot in column])):
        return True

    # Unable to find a match of with 3 of the same letters
    return False

def welcome_screen():
    # Print welcome screen to introduce game to the users.
    print("\n\n**************************** Welcome to Tic Tac Toe ****************************")
    print("--------------------------------------------------------------------------------")
    print("The Rules:")
    print("* Each player will go one at a time, being assigned a single unique letter each.")
    print("* The objective of the game is to get 3 of your letters in a single\nrow/line and you will be dubbed the winner.")
    print("* If nobody is able to get 3 in a row, the game will end in a tie, good luck!!!\n")

def end_screen(n):
    # Print ending screen after completeing the game.
    print(f"\n*********************************** {n} ***********************************")
    print("--------------------------------------------------------------------------------")

def play_tictactoe(player_1, player_2):
    """
    Play a game with Tic-Tac-Toe with either another person
    or against the computer

    Returns the winner of the game or None for a tie
    """
    game = createVals()
    board_outline()
    char = 'X'

    # The loop will continuously play asking users to make a move
    # until all squares have been filled.
    while is_empty(game):
        if (char == 'O'):
            square = player_2.get_move(game)
        else:
            square = player_1.get_move(game)

        if (make_move(game, square, char)):
            print(f'{char} makes a move to square {square}')
            board(game)
            print('') # Space everyting out evenly

            if (check_winner(game, square, char)):
                return f"{char} WINNER"

            # Switch between letters after user makes a move
            if (char == 'X'):
                  char = 'O'
            else:
                  char = 'X'

    # If the loop has all squares filled and wasn't able to determine a winner
    # return a Tie match
    return f"TIE GAME"

def main():
    player_1 = PlayerH('X')
    player_2 = PlayerH('O') # Play against another person
    player_3 = PlayerC('O') # Play the computer
    welcome_screen()
    outcome = play_tictactoe(player_1, player_2)
    end_screen(outcome)

if (__name__ == "__main__"):
    main()
