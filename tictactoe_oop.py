"""Object-oriented tictactoe game"""
from __future__ import print_function
from random import randint
import os


class Board(object):
    """
    Everything conneted to the board in tictactoe game
    """

    def __init__(self, array):
        self.array = array
        self.position = 0
        self.marker = ''

    def display_board(self):
        """
        Function prints a board. Board set up as a list, where each index 1-9
        corresponds with a number on a number pad (you get 3 by 3 board
        representation)
        """
        print(("\n|{b[0]}|{b[1]}|{b[2]}|\n"\
               "|{b[3]}|{b[4]}|{b[5]}|\n"
               "|{b[6]}|{b[7]}|{b[8]}|\n").format(b=self.array))

    def place_marker(self, marker, position):
        """
        Function takes in the board list object, a marker (X or O) and a
        desired position (number 1-9) and assigns it to the board
        """
        if self.space_check(position):
            self.array[position] = marker

    def win_check(self, marker):
        """
        Takes in a board and a mark (X or O) and then checks to see if that
        mark has won
        """
        array = self.array
        if (array[0] == array[1] == array[2] == marker) or\
           (array[3] == array[4] == array[5] == marker) or\
           (array[6] == array[7] == array[8] == marker) or\
           (array[0] == array[3] == array[6] == marker) or\
           (array[1] == array[4] == array[7] == marker) or\
           (array[2] == array[5] == array[8] == marker) or\
           (array[0] == array[4] == array[8] == marker) or\
           (array[2] == array[4] == array[6] == marker):
            return True
        else:
            return False

    def space_check(self, position):
        """
        Returns a boolean indicating whether a space on the board is freely
        available
        """
        return self.array[position] in range(1, 10)

    def full_board_check(self):
        """
        Checks if the board is full and returns a boolean value. True if full,
        False otherwise
        """
        for i in range(0, 9):
            # if self.space_check(self.array, i):
            if self.space_check(i):
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
    Creates a player with a marker 'X' or 'O' as an attribute
    """
    def __init__(self, marker=''):
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

    def player_choice(self, board):  # array zamiast board? w ogole SAMO self?
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
    def __init__(self):
        pass
    # tutaj powinna byc plansza, mozna dac atrybuty typy self.player1_score itp
    # czy inicjalizacja obiektu z tej klasy to bedzie po prostu kazda nowa gra?
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

    def who_plays_first(self):
        """
        Randomly chooses which player plays first
        """
        return randint(1, 2)

    def play(self, player, board, turn): #jakos inaczej trzeba te argumenty
        """
        One turn in the game for a chosen player
        """
        global game_on
        game_on = True
        os.system('clear')
        board.display_board()
        print("\nIt's Player {}'s turn.\n".format(turn))
        position = player.player_choice(board)
        if board.space_check(position):
            board.place_marker(player.marker, position)
            if board.win_check(player.marker):
                board.display_board()
                print("Congrats, Player {}! You have won the game!".format(turn))
                game_on = False
            else:
                if board.full_board_check():
                    board.display_board()
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = 1 if turn == 2 else 2
        return turn, game_on #, tie


def main():
    """
    Setting up the game
    """
    os.system('clear')
    print("\n***********************\n"\
            "Welcome to Tic Tac Toe!\n"\
            "***********************\n")
    while True:
        game = Game()  # initialize it here on in while game_on loop?
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        board = Board(array)
        turn = game.who_plays_first()
        print("Player {} - it's your turn to play first!".format(turn))

# ----------------------------------------------------------------------------
# ----------- creating player in a roundabout way ----------------------------
# ----------------------------------------------------------------------------

        if turn == 1:
            player1 = Player()
            if player1.marker == 'X':
                player2 = Player('O')
            else:
                player2 = Player('X')
        else:
            player2 = Player()
            if player2.marker == 'X':
                player1 = Player('O')
            else:
                player1 = Player('X')
        game_on = True
        while game_on:
            if turn == 1:
                game_return = game.play(player1, board, turn)
                turn = game_return[0]
                game_on = game_return[1]

            else:
                game_return = game.play(player2, board, turn)
                turn = game_return[0]
                game_on = game_return[1]
        if not game.replay():
            # game.clear_console()
            print("\nGood game! See you again sometime!")
            break


if __name__ == "__main__":
    main()
