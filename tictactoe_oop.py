"""All functions for tictactoe game"""
from __future__ import print_function
from random import randint
import os

class Board(object):
    """
    Everything conneted to the board in tictactoe game
    """

# ---------------------------------DO OPISANIA -------------------------------
    def __init__(self, array):#, position, marker):
        self.array = array
        self.position = 0
        self.marker = ''


# ---------------------------------DO OPISANIA -------------------------------
    def display_board(self):
        """
        Function prints a board. Board set up as a list, where each index 1-9
        corresponds with a number on a number pad (you get 3 by 3 board
        representation)
        """
        print(("\n|{b[0]}|{b[1]}|{b[2]}|\n"\
               "|{b[3]}|{b[4]}|{b[5]}|\n"
               "|{b[6]}|{b[7]}|{b[8]}|\n").format(b=self.array))


# ---------------------------------DO OPISANIA -------------------------------
    def place_marker(self, marker, position):
        """
        Function takes in the board list object, a marker (X or O) and a
        desired position (number 1-9) and assigns it to the board
        """
        # tu ponizej powinno byc self.space_check() tylko jak argumenty dac???
        # array = self.array
        if self.space_check(self.array, position):
            # if space_check(self.array, position):
            self.array[position] = marker


# ---------------------------------DO OPISANIA -------------------------------
    def win_check(self, marker):
        """
        Takes in a board and a mark (X or O) and then checks to see if that
        mark has won
        """
        # self.array zamiast board
        array = self.array
        if (array[0] == array[1] == array[2] == marker) or\
           (array[3] == array[4] == array[5] == marker) or\
           (array[6] == array[7] == array[8] == marker) or\
           (array[0] == array[3] == array[6] == marker) or\
           (array[1] == array[4] == array[7] == marker) or\
           (array[2] == array[5] == array[8] == marker) or\
           (array[0] == array[4] == array[8] == marker) or\
           (array[2] == array[4] == array[6] == marker):
            print("Congrats! You have won the game!")
            return True
        else:
            return False


# ---------------------------------DO OPISANIA -------------------------------
    def space_check(self, position):
        """
        Returns a boolean indicating whether a space on the board is freely
        available
        """
        return self.array[position] in range(1, 10)

# ---------------------------------DO OPISANIA -------------------------------
    def full_board_check(self):
        """
        Checks if the board is full and returns a boolean value. True if full,
        False otherwise
        """
        for i in range(0, 9):
            if self.space_check(self.array, i):
                return False
        return True

# ----------------------------------------------------------------------------
#                            JUST FOR TESTING
# ----------------------------------------------------------------------------
    def get_data(self):
        """
        To see what attributes the board has
        """
        return self.array, self.position, self.marker

# ----------------------------------------------------------------------------

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
        """
        Shows which marker the player has
        """
        return self.marker

# ---------------------------------DO OPISANIA -------------------------------

    def player_choice(self, board): #array zamiast board? w ogole SAMO self?
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
    Everything conneted to the game itself
    """
# ---------------------------------DO OPISANIA -------------------------------
    def __init__(self):
        pass
    #tutaj powinna byc plansza, mozna dac atrybuty typy self.player1_score itp
    #czy inicjalizacja obiektu z tej klasy to bedzie po prostu kazda nowa gra?
    # bo nie chce miec tworzonego nowego obiektu "gra" za kazdym razem jak np.
    # jest replay

    def new_game(self):
        """
        Creating new game of tictactoe
        """
        pass

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
        who_is_first = randint(1, 2)
        if who_is_first == 1:
            return 'Player 1'
        return 'Player 2'

def main():
    """
    Setting up the game
    """
    print("\n***********************\n"\
            "Welcome to Tic Tac Toe!\n"\
            "***********************\n")

# ---------------------------------DO OPISANIA -------------------------------
    while True:
        array = [1, 'X', 3, 4, 5, 6, 7, 8, 9]
        board = Board(array)
        board.display_board()
        print(board.get_data())
        game_on = True
        print(board.space_check(1))  # test metody board.space_check()
        game = Game()  # initialize it here on in while game_on loop?
        print(game.who_plays_first() + " - it's your turn to play first!")
        player1 = Player()
        if player1.marker == 'X':
            player2 = Player('O')
        else:
            player2 = Player('X')
        print(player1.marker, player2.marker)
        while game_on:
            # board = Board()
            # print(board.get_data())
            game_on = False
        if not game.replay():
            # game.clear_console()
            print("\nGood game! See you again sometime!")
            break

if __name__ == "__main__":
    main()
