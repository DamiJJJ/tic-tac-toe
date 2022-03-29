def display_board(board):
    # Funkcja, ktora przyjmuje jeden parametr zawierajacy biezacy stan tablicy
    # i wyswietla go w oknie konsoli.
    rows = len(board)
    print("+-------+-------+-------+")
    for r in range(rows):
        print("|       |       |       |")
        print("|  ", board[r][0], "  |  ", board[r][1], "  |  ", board[r][2], "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")
    


# def enter_move(board):
    # Funkcja, ktora przyjmuje parametr odzwierciedlajacy biezacy stan tablicy,
    # prosi uzytkownika o wykonanie ruchu, 
    # sprawdza dane wejsciowe i aktualizuje tablice zgodnie z decyzja uzytkownika.


# def make_list_of_free_fields(board):
    # Funkcja, ktora przeglada tablice i tworzy liste wszystkich wolnych pol; 
    # lista sklada sie z krotek, a kazda krotka zawiera pare liczb odzwierciedlajacych rzad i kolumne.


# def victory_for(board, sign):
    # Funkcja, ktora dokonuje analizy stanu tablicy w celu sprawdzenia
    # czy uzytkownik/gracz stosujacy "O" lub "X" wygral rozgrywke.


# def draw_move(board):
    # Funkcja, ktora wykonuje ruch za komputer i aktualizuje tablice.


board = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
display_board(board)

