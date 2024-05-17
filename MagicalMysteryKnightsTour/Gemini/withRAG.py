#! /usr/bin/python3

from collections import deque

MOVES = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def is_valid_move(board, row, col):
  """Checks if a move is within the board boundaries."""
  return 0 <= row < 8 and 0 <= col < 8 and board[row][col] == -1

def get_available_moves(board, row, col):
  """Returns a list of valid moves sorted by the number of available onward moves."""
  moves = []
  for move in MOVES:
    new_row, new_col = row + move[0], col + move[1]
    if is_valid_move(board, new_row, new_col):
      moves.append((new_row, new_col, len(get_available_moves(board, new_row, new_col))))
  moves.sort(key=lambda x: x[2])  # Sort by the number of available onward moves
  return [move[0:2] for move in moves]  # Return only row and col coordinates

def calculate_row_sum(board):
  """Calculates the sum of values in a row."""
  return sum(row for row in board)

def solve(board, row, col, target_sum):
  """Solves the Knight's tour using constraint propagation and backtracking."""
  n = len(board)

  def get_available_moves_with_updates(r, c):
    """Returns available moves and updates unavailable moves for neighbors."""
    moves = []
    for move in MOVES:
      new_row, new_col = r + move[0], c + move[1]
      if 0 <= new_row < n and 0 <= new_col < n and board[new_row][new_col] == -1:
        moves.append((new_row, new_col))
        for n_row, n_col in MOVES:
          neighbor_row, neighbor_col = new_row + n_row, new_col + n_col
          if 0 <= neighbor_row < n and 0 <= neighbor_col < n:
            board[neighbor_row][neighbor_col] = -2  # Mark neighbor as unavailable

    return moves

  def undo_move(r, c, unavailable_moves):
    """Undoes a move by resetting the value and removing temporary marks on neighbors."""
    board[r][c] = -1
    for row, col in unavailable_moves:
      board[row][col] = -1

  stack = [(row, col, get_available_moves_with_updates(row, col))]

  while stack:
    current_row, current_col, available_moves = stack.pop()

    if current_row == 7 and current_col == 7 and len(available_moves) == 0:
      return calculate_row_sum(board) == target_sum

    # Check constraints: Early termination for invalid states (optional)
    # ... (consider adding checks based on remaining squares or row sums)

    for next_row, next_col in available_moves:
      unavailable_moves = get_available_moves_with_updates(next_row, next_col)
      board[current_row][current_col] = len(board) * current_row + current_col + 1
      stack.append((next_row, next_col, unavailable_moves))
      if solve(board, next_row, next_col, target_sum):
        return True
      undo_move(next_row, next_col, unavailable_moves)
  return False

def main():
  """Reads input, solves the puzzle, and prints the output."""
  board = [[-1 for _ in range(8)] for _ in range(8)]
  target_sum = 0

  for i in range(8):
    row = list(map(int, input().split()))
    board[i] = row
    target_sum += sum(filter(lambda x: x != -1, row))

  if solve(board, 0, 0, target_sum):
    for row in board:
      print(*row, sep=" ")
  else:
    print("No solution")

if __name__ == "__main__":
  main()
