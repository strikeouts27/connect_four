# This my development process for how I created my connect 4 game.

Develop the game logic first and define the function names first. Than build the functions.
That way you are not confused.

Establish board pieces

Player_O = 0
Player_X = X
Player_Y = Y
Player_Z = Z

Empty_Space = '.'

Column_Labels = "1","2","3","4","5","6","7"
Row_Labels = "1","2","3","4","5","6","7"

def main()

player_turn = X

introduce_game_function
"hello welcome to connect four!"
input() how many players are we playing today?

I am thinking if and input statements

def introduce_game()
Input the number of players, in this case we want up to 4.

if two player game 2 players if three than 3 players if four players than 4 players.

if code for two player game under one if statement

elif code for three player game under elif 

elif code for four player game for four player game: 

elif "QUIT" to quit the loop

else: "invalid selection"


if not a valid answer than tell them to pick it again.
if quit than quit.

Turn order logic
Please type in the desired turn order by player number.
input = player_turn_order = variable.
have a confirmation step (the player order is 1,2,3,4 is this correct? if 'y' than lets play if 'n'
than take them back to the main menu and start over. if not a valid response than say give me a valid response)

(in the case of the outline lets do 1,2,3,4 turn order)

I want display the board and ask the player.
'player {1}, please select which column number you want to place your tile into.
a number for your column.

I want python to evaluate the board to see if there is an available space in that column.
If the selection has made that player a winner.
If the selection was a valid one, if not I need the program to inform the player and bring it back to the loop.
If the board is completley full and the game must be declared a draw.
If none of the conditions are met than the tile is updated on the board.

Than I need the next player to have their turn via the turn order logic.

Eventually a winner is declared and the game exits!
