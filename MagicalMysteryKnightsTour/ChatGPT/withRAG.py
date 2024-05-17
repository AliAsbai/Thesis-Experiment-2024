import sys

def is_valid_move(board, row, col, move):
    if 0 <= row + move[0] < 8 and 0 <= col + move[1] < 8:
        return board[row + move[0]][col + move[1]] == -1
    return False

def get_moves(board, row, col):
    moves = []
    for move in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        if is_valid_move(board, row, col, move):
            count = 0
            for next_move in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
                if is_valid_move(board, row + move[0], col + move[1], next_move):
                    count += 1
            moves.append((move, count))
    moves.sort(key=lambda x: x[1])
    return [move[0] for move in moves]

def knight_tour(board, row, col, move_count, memo):
    if move_count == 64:
        return True

    if (row, col) in memo:
        if move_count > memo[(row, col)]:
            return False

    for move in get_moves(board, row, col):
        board[row + move[0]][col + move[1]] = move_count + 1
        if knight_tour(board, row + move[0], col + move[1], move_count + 1, memo):
            return True
        board[row + move[0]][col + move[1]] = -1

    return False

def find_start_position(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                return i, j

def main():
    board = []
    for line in sys.stdin:
        row = [int(x) for x in line.split()]
        board.append(row)

    start_row, start_col = find_start_position(board)
    memo = {}
    knight_tour(board, start_row, start_col, 1, memo)

    for row in board:
        print(' '.join(str(x) for x in row))

if __name__ == "__main__":
    main()
