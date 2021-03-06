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
        if self.is_space_free(position):
            self.array[position] = marker

    def has_it_won(self, marker):
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

    def is_space_free(self, position):
        """
        Returns a boolean indicating whether a space on the board is freely
        available
        """
        return self.array[position] in range(1, 10)

    def is_board_full(self):
        """
        Checks if the board is full and returns a boolean value. True if full,
        False otherwise
        """
        for i in range(0, 9):
            if self.is_space_free(i):
                return False
        return True


class Player(object):
    """
    Creates a player with a marker 'X' or 'O' as an attribute
    """
    def __init__(self, marker=''):
        self.marker = marker
        if self.marker not in ('X', 'O'):
            self.choose_marker()

    def choose_marker(self):
        """
        Function can take in a player input and assign their marker as X or O
        (use while loops to continually ask until you get a correct answer)
        """
        self.marker = input("Do you want to use X or O? ").upper()
        while self.marker not in ('X', 'O'):
            self.marker = input("Please use the correct sign: "\
                                "either X or O\n").upper()

    def get_marker(self):
        """
        Shows which marker the player has
        """
        return self.marker

    def choose_position(self, board):
        """
        Function asks for a player's next position (as a number 1-9) and then
        uses the function is_space_free if it's a free position. If it is, then
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
        answer = input("\nDo you want to play again? [y/n] ").lower()
        while answer not in ('y', 'n'):
            answer = input("Please answer with either y or n.\n"\
                        "Do you want to play again? [y/n] ")
        if answer == 'y':
            os.system('clear')
            return True
        elif answer == 'n':
            return False

    def who_plays_first(self):
        """
        Randomly chooses which player plays first
        """
        return randint(1, 2)

    def play(self, player, board, turn):
        """
        One turn in the game for a chosen player
        """
        game_on = True
        os.system('clear')
        board.display_board()
        print("\nIt's Player {}'s turn.\n".format(turn))
        position = player.choose_position(board)
        if board.is_space_free(position):
            board.place_marker(player.marker, position)
            if board.has_it_won(player.marker):
                board.display_board()
                print("Congrats, Player {}! You have won the game!".format(turn))
                game_on = False
            else:
                if board.is_board_full():
                    board.display_board()
                    print("It's a tie!")
                    game_on = False
                else:
                    turn = 1 if turn == 2 else 2
        return turn, game_on


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

        if turn == 1:
            player1 = Player()
            player2 = Player('O') if player1.marker == 'X' else Player('X')
        else:
            player2 = Player()
            player1 = Player('O') if player2.marker == 'X' else Player('X')
        game_on = True
        while game_on:
            if turn == 1:
                turn, game_on = game.play(player1, board, turn)
            else:                
                turn, game_on = game.play(player2, board, turn)
        if not game.replay():
            print("\nGood game! See you again sometime!")
            break


if __name__ == "__main__":
    main()
