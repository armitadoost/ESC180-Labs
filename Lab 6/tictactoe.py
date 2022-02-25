'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

# Problem 1a
def find_coord(square_num):
    global coord
    row = ((square_num - 1) // 3)
    column = square_num - (3*row)

    coord = [row, column]
    return coord

# Problem 1b
def put_in_board(board, mark, square_num):

    find_coord(square_num)

    board[coord[0]][coord[1]] = mark


# Problem 2a
def get_free_squares(board):
    global free_squares
    free_squares = []

    for i in range(0,3):
        for x in range(0,3):
            if board[i][x] == " ":
                free_squares.append([i,x])

    return free_squares


# Problem 2b, 2c -- fixed algorithm here
def make_random_move(board, mark):

    get_free_squares(board)

    picked_num = random.choice(free_squares)

    board[picked_num[0]][picked_num[1]] = mark

# Problem 3a
def is_row_all_marks(board, row_i, mark):
    global count1
    count1 = 0
    for i in range(0,3):
        if board[row_i][i] == mark:
            count1 += 1
    if count1 == 3:
        return True
    return False

# Problem 3b
def is_col_all_marks(board, col_i, mark):
    global count2
    count2 = 0
    for i in range(0,3):
        if board[i][col_i] == mark:
            count2 += 1
    if count2 == 3:
        return True
    return False


# Problem 3c
def is_win(board, mark):
    win = False
    if board[0][0] == board[1][1] == board[2][2] == mark:
        win = True

    if board[2][0] == board[1][1] == board[0][2] == mark:
        win = True

    for i in range(0,3):
        if is_col_all_marks(board, i, mark) == True or is_row_all_marks(board, i, mark) == True:
            win = True

    return win


# Problem 4 -- I tried my best for it but I can't figure out how to implement it

def computer_alg(mark):
    test = True
    while test:
        get_free_squares(board)
        picked_num = random.choice(free_squares)
        board[picked_num[0]][picked_num[1]] = mark

        if is_win(board, mark) == True:
            test = False

        else:
            board[picked_num[0]][picked_num[1]] = " "
            make_random_move(board, mark)
            test = False



if __name__ == '__main__':

    #Problem 1c
    count = 0
    run = True
    board = make_empty_board()
    print_board_and_legend(board)
    print("\n\n")

    while run:
        move = int(input("Enter your move: "))
        print("\n\n")

        put_in_board(board, "X" , move)

        computer_alg("O")

        print_board_and_legend(board)

        if is_win(board, "X") == True or is_win(board, "O") == True:
            run = False
            print("The game has finished")







