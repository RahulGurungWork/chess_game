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

def is_occupied(x, y):
    try:
        return chess_board[x][y] is not None
    except:
        print("Move is out of bounds")

def is_move_on_same_square(initial_position_x, initial_position_y, moved_position_x, moved_position_y):
    return initial_position_x == moved_position_x and initial_position_y == moved_position_y


def get_possible_moves(x, y):
    piece = chess_board[x][y]
    possible_moves = []
    
    if piece is None:
        return possible_moves

    if piece.endswith("pawn"):
        direction = -1 if piece.startswith("white") else 1
        start_row = 6 if piece.startswith("white") else 1

        if is_in_bounds(x, y + direction) and not is_occupied(x, y + direction):
            possible_moves.append((x, y + direction))
            if y == start_row and not is_occupied(x, y + 2 * direction):
                possible_moves.append((x, y + 2 * direction))

        
        if is_in_bounds(x - 1, y + direction) and is_occupied(x - 1, y + direction) and chess_board[x - 1][y + direction].split('-')[0] != piece.split('-')[0]:
            possible_moves.append((x - 1, y + direction))
        if is_in_bounds(x + 1, y + direction) and is_occupied(x + 1, y + direction) and chess_board[x + 1][y + direction].split('-')[0] != piece.split('-')[0]:
            possible_moves.append((x + 1, y + direction))
    elif piece.endswith("rook"):

  
     if piece == "rook":
        possible_moves.extend(get_linear_moves(x, y, [(1, 0), (-1, 0), (0, 1), (0, -1)], color))

    elif piece == "bishop":
        possible_moves.extend(get_linear_moves(x, y, [(1, 1), (1, -1), (-1, 1), (-1, -1)], color))

    elif piece == "knight":
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for direction_x, direction_y in knight_moves:
            if is_in_bounds(x + direction_x, y + direction_y) and (not is_occupied(x + direction_x, y + direction_y) or chess_board[x + direction_x][y + direction_y].split('-')[0] != color):
                possible_moves.append((x + direction_x, y + direction_y))

    elif piece == "queen":
        possible_moves.extend(get_linear_moves(x, y, [(1, 0), (-1, 0), (0, 1), (0, -1)], color))
        possible_moves.extend(get_linear_moves(x, y, [(1, 1), (1, -1), (-1, 1), (-1, -1)], color))

    elif piece == "king":
        king_moves = [
            (1, 0), (1, 1), (1, -1),
            (0, 1), (0, -1),
            (-1, 0), (-1, 1), (-1, -1)
        ]
        for direction_x, direction_y in king_moves:
            if is_in_bounds(x + direction_x, y + direction_y) and (not is_occupied(x + direction_x, y + direction_y) or chess_board[x + direction_x][y + direction_y].split('-')[0] != color):
                possible_moves.append((x + direction_x, y + direction_y))

    return possible_moves

def get_linear_moves(initial_position_x, initial_position_y, directions, color):
    possible_moves = []
    for direction_x, direction_y in directions:
        moved_position_x, moved_position_y = initial_position_x + direction_x, initial_position_y + direction_y
        while is_in_bounds(moved_position_x, moved_position_y):
            if is_occupied(moved_position_x, moved_position_y):
                if chess_board[moved_position_x][moved_position_y].split('-')[0] != color:
                    possible_moves.append((moved_position_x, moved_position_y))
                break
            possible_moves.append((moved_position_x, moved_position_y))
            moved_position_x += direction_x
            moved_position_y += direction_y
    return possible_moves
    

# archive

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


# testing 

clear_console()
print_board()
print()
move_piece(1,0,2,0)
print_board()