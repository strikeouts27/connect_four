# ASK OURSELVES WHAT PARTS DO WE NEED TO CREATE THIS PROJECT?

# Establish how the tile pieces will be shown on the board.

EMPTY_SPACE = '.'
PLAYER_X = "X"
PLAYER_O = "O"


# Establish the boards dimensons with variables and a test.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6 
COLUMN_LABELS = ("1","2","3","4","5","6","7")
assert(len(COLUMN_LABELS == BOARD_WIDTH))

# establish game logic with main()
def main():
# New game needs to start with the rules being to be shown to the players.
    gameboard = getNewBoard()
    print(""" Hello and welcome to connect four! In order to win this game you need
        to place four tiles in a row horizontally or vertically before your opponent does.
        Each player will get to place one tile on the board until the victory condition is met. """)
    
    player_turn = PLAYER_X
# the player turn needs to be established. 
    def turnlogic(player_tile, board):
        input("Player {} please select a column to place your tile.").format(player_tile)
        # board gets updated based on the selection. 
        # than the turn order changes. 
    
    # the BOARD_HEIGHT - 3 is limiting the victory checker from checking values outside of the
    # boards capacity.
    #  
    def isWinner(playerTile, gameBoard):

        # Go through the entire board, checking for four-in-a-row:

        for columnIndex in range(BOARD_WIDTH - 3): 
            for rowIndex in range(BOARD_HEIGHT):
                tile1 = board[(columnIndex, rowIndex)]
                tile2 = board[(columnIndex + 1, rowIndex)]
                tile3 = board[(columnIndex + 2, rowIndex)]
                tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True 
    
        
        # vertical victory four-in-a-row going down:
        for columnIndex in range(BOARD_HEIGHT - 3):
            for rowIndex in range(BOARD_WIDTH -3):
                tile1 = board[([columnIndex], [rowIndex])]
                tile2 = board[([columnIndex], [rowIndex + 1])]
                tile3 = board[([columnIndex], [rowIndex + 2])]
                tile4 = board[([columnIndex], [rowIndex + 3])]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True 
            
        # checking for right-down victory

        # checking for left-down victory












# while logic runs the game loop. 
while True: 
# The game starts with the empty board being displayed to the user.

# playerMove function activates asking the first player to make a turn.
# gameBoard[playerMove] = playerTurn

# Check for a win or a tie logic
# win function logic check
# tie function logic check
# switch turn to other player

# OKAY ONCE THE LOGIC FOR THE GAME IS MADE WE NEED TO
# ASK OURSELVES WHAT FUNCTIONS WE NEED TO IMPLEMENT IDEAS. 

# functions for the game

# I need a function for creating the board
# I need a function for displaying the board to the user
# I need a function for asking the player to move
# I need a function to determine if a winner should be declared.

# main() requirements

# getNewBoard()

    def turnlogic(player_turn):
        player_turn = PLAYER_X
        if player_turn == PLAYER_X:
        elif player_turn == PLAYER_X: 




