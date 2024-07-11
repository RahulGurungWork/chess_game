#Board
board = [0] * 8

for row in range (len(board)):
    board[row] = ["  "] * 8

#Pieces
white_pieces_map = {
    "wP": [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7)],
    "wR": [(7,0),(7,7)],
    "wN": [(7,1),(7,6)],
    "wB": [(7,2),(7,5)],
    "wQ": [(7,3)],
    "wK": [(7,4)]
}

black_pieces_map = {
    "bP": [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)],
    "bR": [(0,0),(0,7)],
    "bN": [(0,1),(0,6)],
    "bB": [(0,2),(0,5)],
    "bQ": [(0,3)],
    "bK": [(0,4)]
}

col_map = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7

}

def place_pieces():
    for piece, squares in white_pieces_map.items():
        for square in squares:
            x, y = square[0], square[1]
            board[x][y] = piece
            
    for piece, squares in black_pieces_map.items():
        for square in squares:
            x, y = square[0], square[1]
            board[x][y] = piece

place_pieces()

#Printing 
def print_board():
    for i, row in enumerate(board):
        print(8-i, end = ": ")
        for j, col in enumerate(row):
            print(col, end = " ")
        print("\n")
    print(" " * 3 + "a" + " " * 2 + "b" + " " * 2 + "c" + " " * 2 + "d" + " " * 2 + "e" + " " * 2 + "f" + " " * 2 + "g" + " " * 2 + "h")



#Turns and Move Pieces on each turn
current_turn = 1
while True:
    print_board()
    print("")

    current_player = ""

    if current_turn % 2 == 1:
        current_player = "White"
    else:
        current_player = "Black"
    print("")
    print(current_player + " to move.")

    
    starting_square = input("What Piece? : ")
    start_x, start_y = starting_square[0], starting_square[1]
    start_x = col_map[start_x]
    start_y = 8 - int(start_y)
    start_x, start_y = start_y, start_x

    ending_square = input("Where to? : ")
    end_x, end_y = ending_square[0], ending_square[1]
    end_x = col_map[end_x]
    end_y = 8 - int(end_y)
    end_x, end_y = end_y, end_x

    board[end_x][end_y] = board[start_x][start_y]
    board[start_x][start_y] = "  "
   

    