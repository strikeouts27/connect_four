import random, os, time
import sys
# hopefully I do not need from minimax import Minimax

EMPTY_SPACE = '.'
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
player_icon_list = ['X','O','#','$', '*', '!', '@', '&']

COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

def main():
    # outline first
    rules()
    number_of_players = determine_num_players()
    assign_player_icon(number_of_players)
    # start the turns and game
    current_turn = 0
    create_board()
    board = displayBoard(board)
    get_players()
    # assign each player a value

def assign_player_icon(number_of_players):
    game_turn_order = []
    for icon_choice in range(number_of_players):
        while True:
            response = input(f"Player please choose your player icon for marking your selections on the game board {player_icon_list}")
            if input not in player_icon_list:
                print("Please choose from one of the symbols listed in the input.")
                break
            else: 
                input in player_icon_list
                game_turn_order.append(icon_choice)
                player_icon_list.remove(icon_choice)
                continue
                
        

def column_full():
    pass

def create_board():
    board = {}
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board

def determine_num_players():
    max_players = len(player_icon_list)
    while True:
        try:
            num_of_players = int(input(f"Please type in the number of players who will be playing today. Please select how many players between 2-{max_players} "))
            if num_of_players >= 2 <= max_players:
                    return num_of_players
        except ValueError:
            pass
        break
        

    # I am only trying to determine the number of players here.
    # not the turn order. 

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

# what can i use to store information?
# number of players
def get_players():
    pass


def rules():
        print("""\n Hello and welcome to connect 4! The goal of this game is to place four tiles on the board in a row before your opponents do. Victory can be achieved vertically, horizontally, or diagonally!""")

def turn_gen(players):
    while True:
        yield from players

# turn this code format into a workable turn generator for your project 

if __name__ == '__main__':
    main()

