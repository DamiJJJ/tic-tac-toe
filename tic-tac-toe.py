#4.6.2.1 PROJECT: Tic-Tac-Toe

from random import randrange

def display_board(board):
    rows = len(board)
    print("+-------+-------+-------+")
    for r in range(rows):
        print("|       |       |       |")
        print("|  ", board[r][0], "  |  ", board[r][1], "  |  ", board[r][2], "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")
    
def enter_move(board):
    ok = False
    while not ok:
        move = input("Wykonaj swój ruch: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Zły ruch - proszę spróbować ponownie!")
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ['O', 'X']
        if not ok:
            print("Pole jest zajęte - proszę spróbować ponownie!")
            continue
    board[row][col] = 'O'

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    if sign == "X":
        who = "komputer"
    elif sign == "O":
        who = "ty"
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
        if board[rc][rc] != sign:
            cross1 = False
        if board[2 - rc][2 - rc] != sign:
            cross2 = False
    if cross1 or cross2:
        return who
    return None



def draw_move(board):
    while True:
        move = randrange(9)
        if move == 5:
            continue
        else:
            for i in board:
                if move in i:
                    index = i.index(move)            
                    i[index] = "X"
            return board                


board = [[1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]]

free = make_list_of_free_fields(board)
playerturn = True
while len(free):
    display_board(board)
    if playerturn:
        enter_move(board)
        victory = victory_for(board, 'O')
    else:
        draw_move(board)
        victory = victory_for(board, 'X')
    if victory != None:
        break
    playerturn = not playerturn
    free = make_list_of_free_fields(board)

display_board(board)
if victory == "ty":
    print("Wygrałeś!")
elif victory == "komputer":
    print("Wygrał komputer!")
else:
    print("Remis!")