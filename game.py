"""
TODO
- Movement
    - basic move of individuel Piece
    - if a piece is in the way
    - if move is on same squre
    - 
- Visual Board
- Potetnial Moves
- Click Detector
- En Passant
- Capturing
- Castling
- Promotion
- Pawn First Move
"""


#Default Variables

chess_board = [
    ["black-rook", "black-knight", "black-bishop", "black-queen", "black-king", "black-bishop", "black-knight", "black-rook"],
    ["black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn"],
    ["white-rook", "white-knight", "white-bishop", "white-queen", "white-king", "white-bishop", "white-knight", "white-rook"]
]


# Print Options

def clear_console():
    for _ in range(100):
        print()

def print_board():
    for row in chess_board:
        print(row)

def print_heading(heading):
    total_spaces = 50
    padding = (total_spaces - len(heading)) // 2
    printed_heading = ("= " * padding) + (heading) + (" =" * padding)
    print(printed_heading)

# Movement

def is_in_bounds(x, y):
     return 0 <= x < 8 and 0 <= y < 8



def move_piece(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
    piece = chess_board[initial_position_x][initial_position_y]
    if piece is not None:
        if is_in_bounds(moved_position_x, moved_position_y):
            if piece.endswith("pawn"):
                if is_pawn_movement_possible(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
                    commit_move(initial_position_x, initial_position_y, moved_position_x, moved_position_y)
            elif piece.endswith("rook"):
                pass

            elif piece.endswith("knight"):
                pass

            elif piece.endswith("bishop"):
                pass

            elif piece.endswith("king"):
                pass

            elif piece.endswith("qeen"):
                pass

def is_pawn_movement_possible(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
    return initial_position_y == moved_position_y and abs(initial_position_x - moved_position_x)== 1

def is_rook_movement_possible(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
    pass

def is_knight_movement_possible(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
    pass

def is_bishop_movement_possible(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
    pass

def is_king_movement_possible(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
    pass

def is_queen_movement_possible(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
    pass

def commit_move(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
    chess_board[moved_position_x][moved_position_y] = chess_board[initial_position_x][initial_position_y]
    chess_board[initial_position_x][initial_position_y] = None

clear_console()
print_board()
print()
move_piece(1,0,2,0)
print_board()