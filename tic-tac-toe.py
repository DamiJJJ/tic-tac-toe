from random import randrange

board = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

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

# def make_list_of_free_fields(board):
    # Funkcja, ktora przeglada tablice i tworzy liste wszystkich wolnych pol; 
    # lista sklada sie z krotek, a kazda krotka zawiera pare liczb odzwierciedlajacych rzad i kolumne.


# def victory_for(board, sign):
    # Funkcja, ktora dokonuje analizy stanu tablicy w celu sprawdzenia
    # czy uzytkownik/gracz stosujacy "O" lub "X" wygral rozgrywke.


def draw_move(board):
    # Funkcja, ktora wykonuje ruch za komputer i aktualizuje tablice.
    if board[1][1] != "X":
        board[1][1] = "X"
        return board
    else:
        move = randrange(9)
        if move != 5:
            for i in board:
                if move in i:
                    index = i.index(move)            
                    i[index] = "X"
            return board



draw_move(board)
display_board(board)
draw_move(board)
display_board(board)
# enter_move(board)


