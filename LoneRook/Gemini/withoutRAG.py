def is_attacked(board, row, col):
  """
  Checks if a square is attacked by a knight.

  Args:
    board: A list of lists representing the chessboard.
    row: Row index of the square.
    col: Column index of the square.

  Returns:
    True if the square is attacked by a knight, False otherwise.
  """
  for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
    new_row, new_col = row + dr, col + dc
    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == 'K':
      return True
  return False

def can_reach_target(board, row, col, target_row, target_col):
  """
  Checks if the rook can reach the target square safely, capturing knights if necessary.

  Args:
    board: A list of lists representing the chessboard.
    row: Row index of the rook's current position.
    col: Column index of the rook's current position.
    target_row: Row index of the target square.
    target_col: Column index of the target square.

  Returns:
    True if the rook can reach the target square safely, False otherwise.
  """
  # Check if rook's starting position and target are both attacked
  if is_attacked(board, row, col) and is_attacked(board, target_row, target_col):
    return False

  # Check path to capture knight attacking the target (same as before)
  clear_path = True
  for i in range(max(row, target_row) + 1, min(row, target_row, default=row)):
    if board[i][col] != '.':
      clear_path = False
      break
  for i in range(max(col, target_col) + 1, min(col, target_col, default=col)):
    if board[row][i] != '.':
      clear_path = False
      break
  if is_attacked(board, target_row, target_col) and not clear_path:
    return False

  # Check movement along rows and columns (same as before)
  for i in range(row + 1, target_row):
    if board[i][col] != '.':
      return False
  for i in range(row - 1, target_row, -1):
    if board[i][col] != '.':
      return False
  for i in range(col + 1, target_col):
    if board[i][col] != '.':
      return False
  for i in range(col - 1, target_col, -1):
    if board[i][col] != '.':
      return False

  return True

def solve(board):
  """
  Solves the rook and knight problem.

  Args:
    board: A list of lists representing the chessboard.

  Returns:
    "yes" if the rook can reach the target square, "no" otherwise.
  """
  rows, cols = len(board), len(board[0])
  rook_row, rook_col = 0, 0
  target_row, target_col = 0, 0

  # Find rook and target positions
  for i in range(rows):
    for j in range(cols):
      if board[i][j] == 'R':
        rook_row, rook_col = i, j
      elif board[i][j] == 'T':
        target_row, target_col = i, j

  if can_reach_target(board, rook_row, rook_col, target_row, target_col):
    return "yes"
  else:
    return "no"

# Read input
rows, cols = map(int, input().split())
board = [list(input()) for _ in range(rows)]

# Solve and
