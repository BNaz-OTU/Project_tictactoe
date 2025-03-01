# Tic-Tac-Toe Game
#### Description:
I created a Tic-Tac-Toe game where either 2 players play against each other
or a user can face-off against the computer.

I've created a total of 4 files for this project, requirement.txt, README.md,
test_project.py and project.py. The README.md contains a thorough explanation
about the project itself. The requirements.txt file contains all the necessary
libraries that are needed to run the programs. The test_project.py contains all
the test functions for the Tic-Tac-Toe game to ensure that everything is running
correctly. The project.py contains all the code/logic to the TicTacToe game.

In the project.py, I created 3 classes: Player, PlayerC, and PlayerH. Player is
the Parent class, whereas PlayerC and PlayerH are the child classes of Parent
class inheriting its initialization function and get_move function. The reason
the get_move() function in the Parent class doesn't have any functionality because
I want the child classes to have their own versions of get_move, but also require
classes that inherit from Player to always have a get_move function.

The PlayerC class is supposed to define the computer/robot playing the game of
TicTacToe if the user decides they want to play againt the computer. It's
implementation of get_move uses the random library to make a choice, so
that when the computer plays it will always be a unique experience everytime.

The PlayerH class is meant for people to play against each other. The get_move
function of this class will ask the user to choose the next location they would like to
mark, in the case they choose an already selected spot or a random value, the try block
will catch the error and will continuosly ask the user to give a more appropriate value.

The createVals function will create a list recording the position of each 'X' and 'O'.
The is_empty function checks if the board has any empty squares remaining. The
board function will always print a board each turn containing all the moves that
have already been made. The board_outline function will appear once at the beginning of
the game showing which numbers correspond to which location on the TicTacToe board, it's
to help user's easily navigate to open spots and strategize. The moves_left function is
used to determine the available spots left on the grid, this is used in the get_move
functions of both Player classes to determine if the selected spot is a valid option.
The make_move function will execute the move of the player if the position happens to be
free. The check_winner function which will go over to see if the user
has gotten 3 matches in a row/line.

There is welcome_screen function that outlines the rules of the game and to help
enhance user interface. There is an end_screen function that is there to outline to
the player that game has finished, who has won and to help enhance the user interface.
There is a play_tictactoe function that neatly organizes the functions that help create the
game and to play TicTacToe. In the event a player has gotten 3 in a row it will display the
winning user, or if nobody made a match in the game it will display a tie.

Within the main function is where all the classes and functions are declared to play the
game.

In the test_project file, I tested 8 functions. test_createVals checks to see if a list of 9
blank spaces are produced. test_make_move checks to see if making a move is properly saved.
test_is_empty checks to see if a list only contains blank spaces. test_check_winner will
check to see if it can detect a match of 3 in a row. The remaining 4 functions simulate a
game between 2 people and is to ensure that everything works correctly. I tested the 3
possible winning scenarios, if the user got a match of 3 in a row or 3 in a column or 3
diagonally. I also tested in the event the game were to reach a tie. These tests all checked
to see the possible outcomes of completing the game. Each test also used a parameter of
monkeypatch, monkeypatch was very useful in testing the project because it allowed pytest to
enter values into the input functions of my program without the need of human input, without
monkeypatch it would have been very difficult to test my program/functions. I initially had
a 9th test function that would check for bad user input, however I abandoned this test
because I already have a try/catch block for my inputs, so it would override the Error
raises. I could remove the try/catch block, but doing that would cause the game to end
prematurely, as a design choice I decided to leave the try/catch block so the program
could work smoothly.

<!-- #### Video Demo:  https://youtu.be/-l_dlH9SvaM -->
