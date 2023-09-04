import sys

BOARD_WIDTH = 7
BOARD_HEIGHT = 6

EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH


def main():
    print(
        """Four in a Row, by Al Sweigart al@inventwithpython.com Two players take turns dropping tiles into one of seven columns, trying to make four in a row horizontally, vertically, or diagonally. """)
    

    # Set up a new game:
    gameBoard = getNewBoard()
    # in this line of code he declares a starting point by making playerTurn equal X.
    playerTurn = PLAYER_X

    while True:  # Run a player's turn.
        # Display the board and get player's move:
        displayBoard(gameBoard)
        # The player move will be determined by the askForPLayerMove function being called.
        # The player turn was established prior to starting the while True loop you can see this up above.
        # gameBoard is also passed in because we want to see the board as is and it is required.
        playerMove = askForPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # Check for a win or tie:
        # isWinner evaluates if the win condition has happened. python checks and if its not the case
        # it moves on to the elif statement.
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)  # Display the board one last time.
            print("Player" + playerTurn + " has won!")
            sys.exit()
        elif isFull(gameBoard):  # the isFull checker runs and declares it a tie!
            displayBoard(gameBoard)  # Display the board one last time.
            print("There is a tie!")
            sys.exit()

        # There does not seem to be an else statement in this code.
        # if statements are run and python checks to see if player turn is set to x and switches
        # over to player 0 and vice versa. The game ends when the end condition is met.

        # Switch turns to other_player:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X


# creating the board
def getNewBoard():
    """Returns a dictionary that represents a Four in a Row board.

    The keys are (columnIndex, rowIndex) tuples of two integers, and the
    values are one of the 'X', 'O' or '.' (empty space) strings."""
    # using for loops we target all of the pieces on the board with these for loops.
    # this seems like a great technique for updating all values in a system.
    board = {}  #
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board


# in the current state we cannot print a dictionary because of the hash values error
# basically the dictionary does not accept mutable things as keys.


def displayBoard(board):
    """Display the board and its tiles on the screen."""
    """Prepare a list to pass to the format() string method for the board template.
    The list holds all of the board's tiles (and empty spaces) going left to right,
    top to bottom"""

    # these for loops are designed to target every space in the board.
    # the board is something we pass in as an argument.
    # this display board converts that dictionary into a printable editiable list
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])
    # the .format() will take our list and format it into a readable and presentable
    # board for our players.

    # Display the board:
    print(
        """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(
            *tileChars
        )
    )


def askForPlayerMove(playerTile, board):
    """Let a player select a column on the board to drop a tile into.
    REturns a tuple of the (column, row) that the tile falls into."""

    while True:
        # Keep asking player until they enter a valid move.
        # place the playerTile or player name in those brackets.
        print("Player {}, enter a column or QUIT:".format(playerTile))
        response = input("> ".upper().strip())

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        # people who do not want to follow directons
        if response not in COLUMN_LABELS:
            print("Enter a number from 1 to {}".format(BOARD_WIDTH))
            continue  # Ask player again for their move. the while loop
            # will continue looping back to the top.

        # Lists start at a 0 based index. if you put 0 down it will subtract by 1 and bring it to -1 value.
        # this would then trigger the while loop to declare the move invalid and force the user to pick another number!
        # The column index code seen below accomplishes this and also adjusts the code for the list indexing.
        # the integer that is passed in is saved as the columnIndex value.
        columnIndex = int(response) - 1  # -1 for 0-based the index.

        # If the column is full, ask for a move again:
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print("That column is full, select another one.")
            continue  # Ask player again for their move while loop will start over from the top.

        # Starting from the bottom, find the first empty space.
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            # if the boards column index and row index have an empty space,
            # return the columnIndex and rowIndex.
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)


def isFull(board):
    """Returns True if the 'board' has no empty spaces, otherwise returns False."""
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False  # Found an empty space, so return False.
    return True  # All spaces are full.


def isWinner(playerTile, board):
    """Returns True if 'playerTile' has four tiles in a row on 'board',
    otherwise returns False."""

    # Go through the entire board, checking for four-in-a-row:
    # the subtraction of three from the board widith is saying that the checker will only
    # check in places where there is enough space to establish a winner.
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            # Check for horizontal four-in-a-row going right:
            # if the tile 1 has a tile 2,3,and 4 right next to it. a horizontal victory
            # has been achieved. a true statement returned and the if condition for the winner
            # will happen.

            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Check for vertical four-in-a-row going down:
            # from the last placed tile check and see if there are three tiles of the same
            # value (player token) below it. because it drops from the top down only there will
            # never be a scenario where a bottom piece connects from the top.

            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    # there must be 4 player tiles with the same value in a row to win.
    # range start, stop, incremental value
    # we need the checker to stop  at Board height - 3 before the end
    #  so that the remaing values will be valid.
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # Check for four-in-a-row going right-down diagonal:
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True
    return False


# IF the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
