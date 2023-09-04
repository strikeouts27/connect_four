import random, os, time
import sys
# hopefully I do not need from minimax import Minimax


PLAYER_1 = '1'
PLAYER_2 = '2'
PLAYER_3 = '3'
PLAYER_4 = '4'
EMPTY_SPACE = '.'

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

def main():
    start_game()
    number_of_players()

def start_game():
        print("""\n Hello and welcome to connect 4! The goal of this game is to place four tiles on the board in a row before your opponents do.
            Victory can be achieved vertically, horizontally, or diagonally!""")


def determine_num_players():
    while True:
        try:
               num_layers = int(input("How many players between 2-4"))
               return num_players
        except ValueError:
            pass

players = get_players(number_of_players)
current_turn = 0
board = create_game_board()
while True:
     current_player = get_current_player(players, current_turn)
     move = get_move(current_player)
     
number_of_players = determine_num_players
def number_of_players():
        while True: 
            print("How many players are going to be playing in this game? Up to four people can play! \n ")
            response = (input('>')).strip().upper()
            if response == "QUIT":
                print("Some other time than. Have a great rest of your day!")
                sys.exit()

            elif response == "2":
                print("Two player game activate! Let us go ahead and decide the turn order!")
                two_player_game()

            elif response == "3":
                print("Three player game activate! Okay {} Please select which column you wish to place your tile in!").format()
                three_player_game()

            elif response == "4":
                print("Four player game activate! Okay {} Please select which column you wish to place your tile in!").format()
                four_player_game()
            else:
                    print("please enter a number from 1-4 or type QUIT to quit!")
                    continue




def two_player_game():
        print("Okay, this will be a two player game!")
        displayBoard()
        number_of_players = 2

def three_player_game():
        print("Okay this will be a three player game!")
        displayBoard()
        number_of_players = 3 

def four_player_game():
        displayBoard()
        number_of_players = 4 
        print("Okay this will be a four player game!")


def two_player_game_turn_logic(number_of_players):
        print("""Please decide which player will go first by typing in the player number of the person who is going first. \n
              for example if player 1 is going first please press 1. For player 2 press 2. """)
        response = input()
        while True:
            if response == 1:
                first_turn = PLAYER_1
                second_turn = PLAYER_2
                player_turn = PLAYER_1
                break

            elif response == 2:
                first_turn = PLAYER_1
                second_turn = PLAYER_2
                player_turn = PLAYER_2

                break
            elif response == "Q":
                print("Players Quit! No contest!")
                sys.exit()
            else:
                print("Please input a valid selection. Or press Q to Quit.")
                continue


def turn_order_logic_three_player_game(number_of_players):
    print("""Please decide which player will go first by typing in the player number of the person who is going first. \n
              for example if player 1 is going first please press 1. For player 2 press 2. For player 3 press 3 """)
    response = input()
    while True:
        if response == 1:
            first_turn = PLAYER_1
            second_turn = PLAYER_2
            player_turn = PLAYER_1
            break

        elif response == 2:
            first_turn = PLAYER_2
            second_turn = PLAYER_3
            third_turn = PLAYER_1
            player_turn = PLAYER_2
            break

        elif response == 3:
             first_turn = PLAYER_3
             second_turn = PLAYER_4
             third_turn = PLAYER_1
             fourth_turn = PLAYER_2
             player_turn = PLAYER_3

        elif response == "Q":
            print("Players Quit! No contest!")
            sys.exit()
        else:
            print("Please input a valid selection. Or press Q to Quit.")
            continue

def turn_order_logic_four_player_game(number_of_players):
    print("""Please decide which player will go first by typing in the player number of the person who is going first. \n
              for example if player 1 is going first please press 1. For player 2 to go first press 2. For player 3 to go first press 3. For player four press four. """)
    response = input()
    while True:
        if response == 1:
            first_turn = PLAYER_1
            second_turn = PLAYER_2
            third_turn = PLAYER_3
            fourth_turn = PLAYER_4

            player_turn = PLAYER_1
            break

        elif response == 2:
            first_turn = PLAYER_2
            second_turn = PLAYER_3
            third_turn = PLAYER_4
            fourth_turn = PLAYER_1
            player_turn = PLAYER_2
            break
        
        elif response == 3:
            first_turn = PLAYER_3
            second_turn = PLAYER_4
            third_turn = PLAYER_1
            fourth_turn = PLAYER_2
            player_turn = PLAYER_3
        
        elif response == 4:
             first_turn = PLAYER_4
             second_turn = PLAYER_1
             third_turn = PLAYER_2
             fourth_turn = PLAYER_3
             player_turn = PLAYER_4

        elif response == "Q":
            print("Players Quit! No contest!")
            sys.exit()
        else:
            print("Please input a valid selection. Or press Q to Quit.")
            continue



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

