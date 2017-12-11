"""All functions for tictactoe game"""
from __future__ import print_function
from random import randint
import os

class Board(object):
    """
    Everything conneted to the board in tictactoe game
    """

# ---------------------------------DO OPISANIA -------------------------------
    def __init__(self):
        pass

# ---------------------------------DO OPISANIA -------------------------------
    def display_board(self):
        """
        Function prints a board. Board set up as a list, where each index 1-9
        corresponds with a number on a number pad (you get 3 by 3 board
        representation)
        """
        print(("\n|{b[0]}|{b[1]}|{b[2]}|\n"\
               "|{b[3]}|{b[4]}|{b[5]}|\n"\
               "|{b[6]}|{b[7]}|{b[8]}|\n").format(b=board))


# ---------------------------------DO OPISANIA -------------------------------
    def place_marker(board, marker, position):
        """
        Function takes in the board list object, a marker (X or O) and a
        desired position (number 1-9) and assigns it to the board
        """
        if space_check(board, position):
            board[position] = marker


# ---------------------------------DO OPISANIA -------------------------------
    def win_check(board, marker):
        """
        Takes in a board and a mark (X or O) and then checks to see if that mark
        has won
        """
        if (board[0] == board[1] == board[2] == marker) or\
            (board[3] == board[4] == board[5] == marker) or\
            (board[6] == board[7] == board[8] == marker) or\
            (board[0] == board[3] == board[6] == marker) or\
            (board[1] == board[4] == board[7] == marker) or\
            (board[2] == board[5] == board[8] == marker) or\
            (board[0] == board[4] == board[8] == marker) or\
            (board[2] == board[4] == board[6] == marker):
            print("Congrats! You have won the game!")
            return True
        else:
            return False


# ---------------------------------DO OPISANIA -------------------------------
    def space_check(board, position):
        """
        Returns a boolean indicating whether a space on the board is freely
        available
        """
        return board[position] in range(1,10)


# ---------------------------------DO OPISANIA -------------------------------
    def full_board_check(board):
        """
        Checks if the board is full and returns a boolean value. True if full,
        False otherwise
        """
        for i in range(0, 9):
            if space_check(board, i):
                return False
        return True

class Player(object):
    """

    """
    def __init__(self, marker = ''):
        self.marker = marker
        if self.marker not in ('X', 'O'):
            self.player_input()

    def player_input(self):
        """
        Function can take in a player input and assign their marker as X or O
        (use while loops to continually ask until you get a correct answer)
        """
        self.marker = input("Do you want to use X or O? ").upper()
        while self.marker not in ('X', 'O'):
            self.marker = input("Please use the correct sign: "\
                                "either X or O\n").upper()
        return self.marker

    def get_marker(self):
        return self.marker

# ---------------------------------DO OPISANIA -------------------------------

    def player_choice(board):
        """
        Function asks for a player's next position (as a number 1-9) and then
        uses the function space_check if it's a free position. If it is, then
        return the position for later use
        """
        position = '0'
        while position.isnumeric() == False or int(position) not in range(1,10):
            position = input("Please choose your next position from "\
                            "available numbers: ")
        position = int(position)-1
        return position

class Game(object):
    """

    """
# ---------------------------------DO OPISANIA -------------------------------
    def __init__(self):
        pass
    #tutaj powinna byc plansza, mozna dac atrybuty typy self.player1_score itp

    def replay(self):
        """
        Asks the player if they want to play again and returns a boolean True
        if they do want to play again
        """
        answer = input("Do you want to play again? [y/n] ").lower()
        while answer not in ('y', 'n'):
            answer = input("Please answer with either y or n.\n"\
                        "Do you want to play again? [y/n] ")
        if answer == 'y':
            return True
        elif answer == 'n':
            return False


    def clear_console(self):
        """
        Cleaning the console
        """
        os.system('clear')

# ---------------------------------DO OPISANIA -------------------------------
    def who_plays_first(self):
        """
        Randomly chooses which player plays first
        """
        who_is_first = randint(0, 1)
        if who_is_first == 0:
            return 'Player 1'
        return 'Player 2'

# -----------------------------------------------
# Setting up the game
# -----------------------------------------------
print("\n***********************\n"\
        "Welcome to Tic Tac Toe!\n"\
        "***********************\n")

# ---------------------------------DO OPISANIA -------------------------------
game = Game()
player1 = Player()
if player1.marker == 'X':
    player2 = Player('O')
else:
    player2 = Player('X')

if not game.replay():
    print("\nGood game! See you again sometime!")
