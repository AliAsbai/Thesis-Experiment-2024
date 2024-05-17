def is_valid_move(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0])

def is_attacked_by_knight(board, row, col):
    directions = [(1, 2), (-1, 2), (1, -2), (-1, -2),
                  (2, 1), (-2, 1), (2, -1), (-2, -1)]
    for dr, dc in directions:
        if is_valid_move(board, row + dr, col + dc) and board[row + dr][col + dc] == 'K':
            return True
    return False

def can_move_safely(board):
    target_row, target_col = None, None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'T':
                target_row, target_col = i, j
                break
        if target_row is not None:
            break
    
    if target_row is None or target_col is None:
        return False
    
    if is_attacked_by_knight(board, target_row, target_col):
        return False
    
    rook_row, rook_col = None, None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                rook_row, rook_col = i, j
                break
        if rook_row is not None:
            break
    
    if rook_row is None or rook_col is None:
        return False
    
    if rook_row == target_row or rook_col == target_col:
        return True
    
    return False

# Reading input
r, c = map(int, input().split())
board = [input() for _ in range(r)]

# Checking if the white rook can move to the target square
if can_move_safely(board):
    print("yes")
else:
    print("no")
