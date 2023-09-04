import random, os, time
import sys
# hopefully I do not need from minimax import Minimax


PLAYER_1 = 'X'
PLAYER_2 = 'O'
PLAYER_3 = 'A'
PLAYER_4 = 'B'
EMPTY_SPACE = '.'

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

def main():
    start_game()
        

def start_game():
        print("""\n Hello and welcome to connect 4! The goal of this game is to place four tiles on the board in a row before your opponents do.
            Victory can be achieved vertically, horizontally, or diagonally!""")

def number_of_players():
        input("How many players are going to be playing in this game? Up to four people can play! \n ")
        response = input('>').upper().strip()
        if response == 2:
            print("Two player game activate!")
            two_player_game()
        elif response == 3:
            three_player_game()
        elif response == 4:
            four_player_game()
        elif response == 'QUIT' & 'EXIT':
            sys.exit()
        


def two_player_game():
        print("Okay, this will be a two player game. Player 1 go ahead and start us off!")

def three_player_game():
        print("This is response 3")

def four_player_game():
        print("This is response 4")

def place_tile():                
        print("{} please select a column to drop your tile into.").format(player_turn)
        input("""Player {}, please select which column you want to place your tile in by typing in 
        its respective number. {}""").format(player_turn) 


# Run a player's turn.
# Display the board and get player's move:
                 




            # column = input('Player {}, enter your move (1-4):').format(current_player)

def is_win():
    print("player {} has placed four tiles in a row and has won the game!")

def create_board():
    board = {}
    for columnIndex in BOARD_HEIGHT:
        for rowIndex in BOARD_WIDTH:
            board[columnIndex, rowIndex] = EMPTY_SPACE
    return board

def displayBoard(board):
    tileChars = []
    for columnIndex in BOARD_HEIGHT:
        for rowIndex in BOARD_WIDTH:
            tileChars.append(board[(columnIndex, rowIndex)])
            print(
            COLUMN_LABELS + """
            |{}{}{}{}{}{}|
            |{}{}{}{}{}{}|
            |{}{}{}{}{}{}|
            |{}{}{}{}{}{}|
            |{}{}{}{}{}{}|
            |{}{}{}{}{}{}|
            |{}{}{}{}{}{}|
            +----------+""".format(*tileChars))

def is_Full():
    # for i in rowcolumn board != EMPTY_SPACE:
        print("The board is full, this game is a tie!")
                    
def column_full():
    pass
                    
def place_tile():
    pass
    # If the program is run (instead of imported), run the game:

if __name__ == '__main__':
    main()

