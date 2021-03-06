#Maayez Imam 11/10/17
#Connect N program

import time
import random

matrix_height = int(input("Enter the number of rows: "))
matrix_width = int(input("Enter the number of columns: "))

connect_n = int(input("Enter the number of pieces in a row to win: "))


def el():  # Empty line - Makes spacing nicer
    print(' ')


def make_board():  # (Re)creates board/grid/matrix
    global board
    board = []

    for x in range(matrix_height):  # Makes [matrix_height] lists each containing [matrix_width + 1] columns.
        board.append(["* "] * (matrix_width + 1))  # +1 for the extra line after the final column


def print_board():

    for row in board:
        print(" ".join(row))  # Joins list elements to form a string, " " means they have a space in between
        # no comma after means that rows are printed one after another (as rows are list items)


def character_select(player):

    while True:  # Repeats until a (length 1) character is chosen.

        el()

        c = input("Player " + str(player) + ", choose your character! ").upper()  # Uppercase looks nicer.

        if c == "NO" or c == "NOPE" or c == "NO THANKS":
            el()
            stubborn = ["You're very stubborn, aren't you?", "Fine, have it your way"]
            print(random.choice(stubborn))
            time.sleep(0.6)
            c = "L"
            print("I'll choose your character for you, since you find it so difficult. ")
            time.sleep(1.1)
            print("It's 'L' by the way. You know, L for Loser.")
            time.sleep(1.2)

            if player == 2:
                if character_1 == "L":
                    c = "A"
                    print("Come to think of it, I'll choose 'A', for A**hole. Much more relevant.")
                    time.sleep(1.4)

        if c == "MAKE ME":
            el()
            make_me = ["Okay then.", "Sure thing.", "With pleasure."]
            print(random.choice(make_me))
            time.sleep(0.5)

        elif len(c) != 1:  # Includes returning nothing awa strings longer than 1
            el()
            if c == "OK" or c == "OKAY" or c == "SURE":
                print("Very funny.")
                time.sleep(0.4)

            if c == "HELLO" or c == "HI" or c == "HELLO WORLD" or c == "SUP":
                print("Hello to you too!")
                time.sleep(0.6)

            not_char = ["Your character must be a character.", "That\'s not a character!", "Try again.",
                        "Character. Literally.", "I'm not going to let you do that. Nothing personal."]
            print(random.choice(not_char))  # Randomly chooses one of above sentences.

            time.sleep(0.6)  # Player sees message before being told to choose column again.

            if c == "TOM" or c == "TOM QUINCEY" or c == "TRQ":
                print("Shame - you had such a great choice!")
                time.sleep(0.5)

        elif c == "." or c == "," or c == "`" or c == "'":
            el()
            print("You should choose a more visible character.")
            time.sleep(0.5)

        else:
            return c


def show_columns():  # Prints row of numbers, showing player which column is which

    for i in range(matrix_width):

        if i + 1 <= 10:
            print(' ' + str(i + 1),)  # Makes spacing right for numbers <=10
        else:
            print(str(i + 1),)  # Makes spacing right for numbers >10
    el()


def choose_column():

    try:
        c = int(input("Choose Column " + '(1-' + str(matrix_width) + '): ')) - 1
    except ValueError:  # Input of strings to choose_column() would break game
        el()
        no_number = ["That's not even a number!", "Pressing a number key really isn't that difficult.",
                     "You somehow managed to miss the board, well done.", "Impressive! Try again."]
        print(random.choice(no_number))
        time.sleep(0.5)
        c = choose_column()

    while c not in range(matrix_width):  # Must be while, not if

        el()
        off_board = ["You missed the board, good job!", "Helpful hint: the board isn't that big.",
                     "Is this how you normally play?", "Is it really that hard?", "Have another go. Aren't I kind?"]
        print(random.choice(off_board))
        time.sleep(0.5)
        c = choose_column()

    return c


def stack_height(cc):  # Finds out how high the stack is, returns height of lowest empty "hole".

    h = matrix_height - 1  # Top row has height 0, row no. increases down the grid. h is now the bottom row.

    while True:

        if h == -1:  # If top row is full (on column), then h = 0-1 = -1
            el()
            too_high = ["The board doesn't go that high. Obviously.", "Try again, genius.",
                        "Do you normally play like this?", "I should make you lose instantly for that."]
            print(random.choice(too_high))  # Player placed counter above matrix
            time.sleep(0.5)
            return -1

        elif board[h][cc] != "| ":  # If there is a character in this hole, look at hole above.
            h -= 1
        else:
            return h  # h is (now) lowest empty hole


def pattern():  # pwetty pattern

    el()
    print ('\*/*' * 8) + '\ '
    print ('/*\*' * 2) + '/ ' + '   YOU WIN!   ' + ('/*\*' * 2) + '/ '
    print ('\*/*' * 8) + '\ '


def play(char):

    el()
    print(str(char) + '\'s ' "turn: ")

    show_columns()
    print_board()

    el()
    cc = choose_column()

    sh = stack_height(cc)

    while sh == -1:  # Player places counter again after attempting to place in a full stack.
        cc = choose_column()
        sh = stack_height(cc)

    board[sh][cc] = "|" + str(char)  # Left half works because 'board' has lists within it's own list. [row][column]

    if find_4(sh, cc):  # If n are connected in a row, stack, or diagonal
        pattern()
        el()
        return True


def play_again():

    time.sleep(1.0)

    while True:
        el()
        replay = input("Do you want to play again? ")

        if replay == 'y' or replay == 'yes' or replay == 'yeah' or replay == 'okay' \
                or replay == 'ok' or replay == 'sure' or replay == '01111001':
            return True
        elif replay == 'n' or replay == 'no' or replay == 'nope' or replay == 'rather not' or replay == 'seriously?':
            return False
        else:
            el()
            other = ["What?", "Pardon?", "I don't understand!", "I haven't been programmed to answer that."]
            print(random.choice(other))
            time.sleep(0.5)


def board_full():  # Finds out if board is full. (Easiest to test with n = 3)

    count = 0
    for x in range(matrix_width):
        if board[0][x] != '| ':  # If the top row is full, therefore the whole board is full.
            count += 1

    if count == matrix_width:
        return True


# --------------------------- FIND SURROUNDING COUNTERS -----------------------------

def left(sh, cc):

    if board[sh][cc] == board[sh][cc - 1]:  # Counter to the left is the same as counter just dropped
        return True


def right(sh, cc):

    if board[sh][cc] == board[sh][cc + 1]:  # Counter to the right is the same as counter just dropped
        return True


def up_left(sh, cc):

    if board[sh][cc] == board[sh - 1][cc - 1]:
        return True


def up_right(sh, cc):

    if board[sh][cc] == board[sh - 1][cc + 1]:
        return True


def down(sh, cc):

    if sh < matrix_height - 1:  # See stack_height() description.
        if board[sh][cc] == board[sh + 1][cc]:  # Two 'ifs' are identical to 'and' (I think this way looks nicer)
            return True


def down_left(sh, cc):

    if sh < matrix_height - 1:  # See stack_height() description.
        if board[sh][cc] == board[sh + 1][cc - 1]:
            return True


def down_right(sh, cc):

    if sh < matrix_height - 1:  # See stack_height() description.
        if board[sh][cc] == board[sh + 1][cc + 1]:
            return True


def find_horizontal_4(sh, cc):

    horiz_count = 1
    tracker_count = 0

    while True:

        if left(sh, cc - tracker_count):  # If counter to left is same, increase horiz_count by 1
            horiz_count += 1
            tracker_count += 1
        else:
            break

    tracker_count = 0  # Resets tracker_count after first while loop.

    while True:

        if right(sh, cc + tracker_count):
            horiz_count += 1
            tracker_count += 1
        else:
            break

    if horiz_count >= connect_n:  # n counters are connected horizontally
        return True


def find_vertical_4(sh, cc):

    vert_count = 1
    tracker_count = 0  # This is slightly redundant as there is only one while loop for find_vertical_4()

    while True:

        if down(sh + tracker_count, cc):
            vert_count += 1
            tracker_count += 1
        else:
            break

    if vert_count >= connect_n:  # n counters are connected vertically
        return True


def find_down_left_4(sh, cc):

    down_left_count = 1
    tracker_count = 0

    while True:

        if down_left(sh + tracker_count, cc - tracker_count):
            down_left_count += 1
            tracker_count += 1
        else:
            break

    tracker_count = 0  # Resets tracker_count after first while loop.

    while True:

        if up_right(sh - tracker_count, cc + tracker_count):
            down_left_count += 1
            tracker_count += 1
        else:
            break

    if down_left_count >= connect_n:  # n counters are connected diagonally (down/left)
        return True


def find_down_right_4(sh, cc):

    down_right_count = 1
    tracker_count = 0

    while True:

        if down_right(sh + tracker_count, cc + tracker_count):
            down_right_count += 1
            tracker_count += 1
        else:
            break

    tracker_count = 0  # Resets tracker_count after first while loop.

    while True:

        if up_left(sh - tracker_count, cc - tracker_count):
            down_right_count += 1
            tracker_count += 1
        else:
            break

    if down_right_count >= connect_n:  # n counters are connected diagonally (down/right)
        return True


def find_4(sh, cc):

    if find_horizontal_4(sh, cc) or find_vertical_4(sh, cc) or find_down_right_4(sh, cc) or find_down_left_4(sh, cc):
        return True

# ----------------------------------  GAME  -----------------------------------------

# Intro
make_board()

print("Let's play Connect " + str(connect_n) + "!")
time.sleep(0.2)

if connect_n >= 7:
    print("Good luck! You'll need it.")
    time.sleep(0.4)

if connect_n <= 2:
    small_n = ["This is going to be an odyssey of a game, I can tell.",
               "Spoiler: Player 1 wins. Bet you didn't see that one coming."]
    print(random.choice(small_n))
    time.sleep(1.0)

character_1 = character_select(1)

character_2 = character_select(2)

while character_2 == character_1:
    el()
    same_char = ["You cannot have the same character as Player 1.", "*sigh*", "Have another go. I feel sorry for you.",
                 "That might make the game a *little* confusing.", "That's not a very good idea, is it?"]
    print(random.choice(same_char))
    time.sleep(0.5)
    character_2 = character_select(2)

# Main Game
while True:

    if play(character_1):  # Still runs play() (which returns True when find_4() == True)
        print_board()  # All this code only runs when [n] counters have been connected.
        el()
        if play_again():
            make_board()
        else:
            break

    if play(character_2):
        print_board()
        el()
        if play_again():
            make_board()
        else:
            break

    if board_full():
        el()
        print_board()
        el()
        time.sleep(0.8)

        for a in range(3):
            print(".",)
            time.sleep(0.5)

        print("Somehow you both managed to lose.",)
        time.sleep(1.0)
        print("Congratulations.",)
        time.sleep(1.0)
        el()

        if play_again():
            make_board()
        else:
            break




# def makeMove(board, numRows, numCols, col, piece):
#       i = int()
#
#       for i in range(numRows - 1):
#            if board[i][col] == '*':
#                   board[i][col] = piece
#                   break
#
#
#       printBoard(board, numRows, numCols)
#
#
# def declareWinner(board, numRows, numCols, turn, numToWin):
#
#       if tied(board, numRows, numCols, numToWin):
#           print("Tie game!\n")
#       elif turn == 0:
#           print("Player 2 Won!\n")
#       else:
#           print("Player 1 Won!\n")
#
#
# def playGame(board, turn, numRows, numCols, numToWin):
#       col = int()
#       pieces = '\XO'
#
#       while not checkGameOver(board, numRows, numCols, numToWin):
#             col = getValidMove(board, numCols)
#             makeMove(board, numRows, numCols, col, pieces[turn])
#             turn = (turn + 1) % 2
#
#       declareWinner(board, numRows, numCols, turn, numToWin)
#
# def main(argc, argv):
#     numRows = int()
#     numCols = int()
#     numToWin = int()
#     turn = int()
#     board = chr
#
#     if(argc != 4):
#         if (argc < 4):
#             print("Not enough arguments entered\n")
#             print("Usage connectn.out num_rows num_columns number_of_pieces_in_a_row_needed_to_win\n")
#             exit(0)
#
#         elif (argc > 4):
#             print("Too many arguments entered\n")
#             print("Usage connectn.out num_rows num_columns number_of_pieces_in_a_row_needed_to_win\n")
#             exit(0)
#         else:
#             input(argv[1], "%d" %numRows)
#             input(argv[2], "%d" %numCols)
#             input(argv[3], "%d" %numToWin)
#
#     setUp(board, turn, numRows, numCols)
#     printBoard(board, numRows, numCols)
#     playGame(board, turn, numRows, numCols, numToWin)
#     cleanUpBoard(board, numRows)
#
#
#     return 0
#
#
# def getValidMove(board, numCols):
#       col = int()
#       numArgsRead = int()
#
#       while not isValidMove(numArgsRead, 1, board, col, numCols):
#           print("Enter a column between 0 and %d to play in: ", numCols-1)
#           numArgsRead = input("%d" %col)
#
#       return col
#
# #bool
# def isValidMove(numArgsRead, numArgsNeeded, board, col, numCols):
#
#       if not isValidFormatting(numArgsRead, numArgsNeeded):
#            return False
#
#       elif not inBounds(col, numCols):
#             return False
#
#       elif board[0][col] != '*':
#             return False
#
#       else:
#             return True
#
# #bool
# def isValidFormatting(numArgsRead, numArgsNeeded):
#     newLine = '\n'
#     isValid = True
#
#     if numArgsRead != numArgsNeeded:
#         isValid = False
#
#     while newLine != '\n':
#         input("%c" %newLine)
#         if not newLine.isspace():
#             isValid = False
#
#     return isValid
#
# #bool
# def inBounds(col, numCols):
#       return col >= 0 and col < numCols
#
# def setUp(board, turn, numRows, numCols):
#       board = makeBoard(numRows, numCols)
#       turn = 0
#
# #char**
# def makeBoard(numRows, numCols)
#
#     board = (char**)malloc(numRows * sizeof(char*))
#     i = int()
#     j = int()
#
#     for i in range(numRows):
#         board[i] = (char*)malloc(numCols*sizeof(char))
#         for j in range(numCols):
#             board[i][j] = '*'
#
#     return board
#
# def printBoard(board, numRows, numCols):
#     i = int()
#     j = int()
#
#     for i in range(numRows):
#         print("%d ", numRows - i -1)
#         for j in range(numCols):
#                 print("%c ", board[i][j])
#         print("\n")
#
#     print("  ")
#
#     for j in range(numCols):
#         print("%d ", j)
#     print("\n")
#
#
# def cleanUpBoard(board, numRows):
#     i = int()
#     for i in range(numRows):
#         free(board[i])
#     free(board)
#
# #bool
# def checkGameOver(board, numRows, numCols, numToWin):
#       return won(board, numToWin, numCols, numRows) or tied(board, numRows, numCols, numToWin)
#
# #bool
# def won(board, numToWin, numCols, numRows):
#       return horizWin(board, numToWin, numCols, numRows) or vertWin(board, numToWin, numCols, numRows) or diagWin(board, numToWin, numCols, numRows)
#
# #bool
# def horizWin(board, numToWin, numCols, numRows):
#     i = int()
#     j = int()
#     k = int()
#     winner = bool
#     firstPiece = chr
#
#     for i in range(numRows):
#         for j in range(numCols - numToWin + 1):
#                 winner = True
#                 firstPiece = board[i][j]
#                 if firstPiece == '*':
#                     continue
#
#                 for k in range(numToWin):
#                     if firstPiece != board[i][j+k]:
#                             winner = False
#                             break
#
#                 if winner:
#                     return True
#
#     return False
#
#
# #bool
# def vertWin(board, numToWin, numCols, numRows):
#     i = int()
#     j = int()
#     k = int()
#     winner = bool
#     firstPiece = chr
#
#     for i in range(numCols):
#         for j in range(numRows - numToWin + 1):
#                 winner = True
#                 firstPiece = board[j][i]
#                 if firstPiece == '*':
#                     continue
#
#                 for k in range(numToWin):
#                     if firstPiece != board[j+k][i] :
#                             winner = False
#                             break
#
#                 if winner:
#                     return True
#
#     return False
#
# #bool
# def diagWin(board, numToWin, numCols, numRows):
#       return leftDiagWin(board, numToWin, numCols, numRows) or rightDiagWin(board, numToWin, numCols, numRows)
#
#
# #bool
# def leftDiagWin(board, numToWin, numCols, numRows):
#     i = int()
#     j = int()
#     k = int()
#     winner = bool
#     firstPiece = chr
#
#     for i in range(numRows - numToWin + 1):
#         for j in range(numCols - numToWin + 1):
#                 winner = True
#                 firstPiece = board[i][j]
#                 if firstPiece == '*':
#                     continue
#
#                 for k in range(numToWin):
#                     if firstPiece != board[i+k][j+k]:
#                             winner = False
#                             break
#
#                 if winner:
#                     return True
#
#     return False
#
# #bool
# def rightDiagWin(board, numToWin, numCols, numRows):
#     i = int()
#     j = int()
#     k = int()
#     winner = bool
#     firstPiece = chr
#
#     for i in range(numRows - numToWin + 1)#(i = numRows - 1; i >= numRows - numToWin + 1; --i) {
#         for j in range(numCols - numToWin + 1):
#                 winner = True
#                 firstPiece = board[i][j]
#                 if firstPiece == '*':
#                     continue
#
#                 for k in range(numToWin):
#                     if firstPiece != board[i-k][j+k]:
#                             winner = False
#                             break
#
#                 if winner:
#                     return True
#
#     return False
#
#
# def tied(board, numRows, numCols, numToWin):
#       return checkBoardFull(board, numRows, numCols) and not won(board, numToWin, numCols, numRows)
#
#
# def checkBoardFull(board, numRows, numCols):
#     i = int()
#     j = int()
#
#     for i in range(numRows):
#         for j in range(numCols):
#                 if board[i][j] == '*':
#                     return False
#
#     return True