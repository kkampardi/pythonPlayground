
""" create a board list using a comprenention """
board = [" " for i in range(9)]


""" print the board """


def print_board():
    row1 = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    row2 = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row3 = '|{}|{}|{}|'.format(board[6], board[7], board[8])

    print ()
    print (row1)
    print (row2)
    print (row3)
    print ()

''' handle player moves '''


def player_move(icon):

    if icon == "X":
        player = 1
    elif icon == "O":
        player = 2

    print("Your turn player {}".format(player))

    choice = int(input("Enter your move(1-9):").strip())
    """ check for valid input """
    while choice > 9 or choice < 1:
        print ("{} is not a valid choice!".format(choice))
        choice = int(input("Enter a valid move(1-9):").strip())

    ''' check if users choice is empty '''
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print
        print ("That space is already taken")

""" handle the draws """


def is_draw():
    if " " not in board:
        return True
    else:
        return False


""" get the winner """
def is_victory(icon):
    if  (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[7] == icon and board[8] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[3] == icon and board[5] == icon and board[8] == icon):
        return True
    else:
        return False


''' main gameplay '''

while True:

    ''' handle players '''
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("Player one wins!")
        break
    elif is_draw():
        print("Its a draw!")
        break

    player_move("O")
    if is_victory("O"):
        print_board()
        print("Player 2 wins!")
        break
    elif is_draw():
        print("It is draw")
        break1



