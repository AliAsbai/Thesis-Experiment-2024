def is_valid_move(board, row, col):
    return 0 <= row < 8 and 0 <= col < 8 and board[row][col] == -1

def is_valid_tour(board):
    row_sums = [sum(row) for row in board]
    col_sums = [sum(col) for col in zip(*board)]
    return all(sum_row == 260 for sum_row in row_sums) and all(sum_col == 260 for sum_col in col_sums)

def get_next_moves(board, row, col):
    next_moves = []
    row_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    col_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    
    for i in range(8):
        next_row = row + row_moves[i]
        next_col = col + col_moves[i]
        
        if is_valid_move(board, next_row, next_col):
            next_moves.append((next_row, next_col))
    
    return next_moves

def solve_knights_tour(board, row, col, num):
    if num == 65:
        return is_valid_tour(board)
    
    next_moves = get_next_moves(board, row, col)
    next_moves.sort(key=lambda move: len(get_next_moves(board, move[0], move[1])))
    
    for next_row, next_col in next_moves:
        board[next_row][next_col] = num
        if solve_knights_tour(board, next_row, next_col, num + 1):
            return True
        board[next_row][next_col] = -1
    
    return False

def fill_missing_labels(input_board):
    board = [list(map(int, row.split())) for row in input_board]
    
    # Find the starting point
    start_row, start_col = None, None
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                start_row, start_col = i, j
                break
        if start_row is not None:
            break
    
    # Start backtracking to fill in the missing labels
    solve_knights_tour(board, start_row, start_col, 2)
    
    # Print the solution
    for row in board:
        print(' '.join(map(str, row)))

input_board = [
    "1 48 -1 -1 33 -1 63 18",
    "30 51 -1 3 -1 -1 -1 -1",
    "-1 -1 -1 -1 15 -1 -1 -1",
    "-1 -1 -1 45 -1 -1 36 -1",
    "-1 -1 25 -1 9 -1 21 60",
    "-1 -1 -1 -1 24 57 12 -1",
    "-1 6 -1 -1 39 -1 -1 -1",
    "54 -1 42 -1 -1 -1 -1 -1"
]

fill_missing_labels(input_board)
