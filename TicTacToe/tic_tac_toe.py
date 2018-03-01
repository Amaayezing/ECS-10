#def play_tic_tac_toe(a: float) -> float: #how to annotate the functions to declare the types for the variables and the return value
import random


def create_board(blank_char : str) -> list:
    the_board = []
    for row in range(3):  #for each row
        a_row = []
        for col in range(3):  #for each column
            a_row.append(blank_char)
        the_board.append(a_row)
    return  the_board


def make_move(move, board):
    pass


def display_board(board: list) -> None:
    pass


def get_move():
    pass


def play_tic_tac_toe() -> None:

    board = create_board()

    player_turn = random.randint(0, 1)

    while not is_game_over():
        display_board(board)
        move = get_move()
        make_move(move, board)
        turn = change_turn(player_turn)
    declare_results(board)

#create a board

#choose who is O and X

#while the game isn't over
#   display the board
#   get a move from the current player
#   make that player's move
#   change the player's turn

#declare a winner or a tie