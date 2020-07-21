#1) We need to be able to display the board, and when we display the board, we need to make sure the dots can be replaced with X or O.
board = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
player = 1
running = 0
win = 1
draw = -1
game = running
X = 'X'
O = 'O'

def drawboard():
    print(" %c | %c | %c " % (board[0], board[1], board[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[3], board[4], board[5]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[6], board[7], board[8]))
    print("   |   |   ")

def CheckWin():
    global game
    #horizontal
    if (board[0] == board[1] and board[1] == board[2] and board[0] != '.'):
        game = win
    elif (board[3] == board[4] and board[4] == board[5] and board[3] != '.'):
        game = win
    elif (board[6] == board[7] and board[7] == board[8] and board[6] != '.'):
        game = win
        #vertical
    elif (board[0] == board[3] and board[3] == board[6] and board[0] != '.'):
        game = win
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != '.'):
        game = win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != '.'):
        game = win
        #diagonal
    elif (board[0] == board[4] and board[4] == board[8] and board[4] != '.'):
        game = win
    elif (board[2] == board[4] and board[4] == board[6] and board[4] != '.'):
        game = win
        #tie
    elif (board[0] != '.' and board[1] != '.' and board[2] != '.' and board[3] != '.' and board[4] != '.' and board[
        5] != '.' and board[6] != '.' and board[7] != '.' and board[8] != '.'):
        game = draw
    else:
        game = running

#3) Check to see if the move is invalid, or if the spot is occupied
def check_availability(z):
    if (board[z] == '.'):
        return True
    else:
        return False

def check_validity(w):
    if (w < 9) :
        return True
    else:
        return False

print("Tic-Tac-Toe Game")
print('''Instructions for the game are as follows:\n
         1. Only one player can play at a time.\n
         2. If any of the players have filled a square then the other player and the same player cannot override that square.\n
         3. There are only two conditions that may match will be draw or may win.\n
         4. The player that succeeds in placing three respective marks (X or O) in a horizontal, vertical, or diagonal row wins the game.\n''')

# Check for player 1's option on picking X or O:
select = input("Player 1 select between 'X' and 'O': ")
if select == X:
    print(" Player 1 is X and Player 2 is O")
    player1_mark = 'X'
    player2_mark = 'O'
elif select == O:
    print("Player 1 is O and Player 2 is X")
    player1_mark = 'O'
    player2_mark = 'X'

#2) Be able to replace dots with X and O. And be able to switch between player 1 and player 2

while (game == running):
    drawboard()
    if (player % 2 != 0):
        print("Player 1")
        mark = player1_mark
    elif (player % 2 == 0):
        print("Player 2")
        mark = player2_mark
    player_option = int(input("Enter the position between (0-8): "))
    if (check_availability(player_option)):
        if (check_validity(player_option)):
            board[player_option] = mark
            player += 1
            CheckWin()
            if (game == win):
                player -= 1
                if (player % 2 != 0):
                    print("Player 1 Won")
                else:
                    print("Player 2 Won")
        else:
            print("PLease enter a number between 0-8.")
    else:
        print("This position is already occupied. Please choose another position.")

drawboard()
if (game == draw):
    print("Game Over! It is a Tie!")