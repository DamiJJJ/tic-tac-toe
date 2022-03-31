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
    while True:
        move = int(input("Wykonaj swój ruch: "))
        if move not in range(1, 10):
            continue
        else:
            for i in board:
                if move in i:
                    index = i.index(move)            
                    i[index] = "O"
            return board

def make_list_of_free_fields(board):
    # Funkcja, ktora przeglada tablice i tworzy liste wszystkich wolnych pol; 
    # lista sklada sie z krotek, a kazda krotka zawiera pare liczb odzwierciedlajacych rzad i kolumne.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free_fields.append((row, col))
    return free_fields

# def victory_for(board, sign):
    # Funkcja, ktora dokonuje analizy stanu tablicy w celu sprawdzenia
    # czy uzytkownik/gracz stosujacy "O" lub "X" wygral rozgrywke.


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

draw_move(board)
# display_board(board)
# enter_move(board)
display_board(board)
print(make_list_of_free_fields(board))

