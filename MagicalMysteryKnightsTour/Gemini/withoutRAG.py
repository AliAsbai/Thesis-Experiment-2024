import random

def get_valid_moves(board, row, col):
  """
  Returns a list of valid knight moves.
  """
  moves = []
  for dx, dy in [(-2, 1), (-2, -1), (1, -2), (1, 2), (-1, 2), (-1, -2), (2, 1), (2, -1)]:
    new_row = row + dx
    new_col = col + dy
    if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row][new_col] == -1:
      moves.append((new_row, new_col))
  return moves

def calculate_row_sum(board, row):
  """
  Calculates the sum of values in a given row.
  """
  return sum(board[row])

def calculate_col_sum(board, col):
  """
  Calculates the sum of values in a given column.
  """
  return sum(row[col] for row in board)

def is_valid_assignment(board, row, col, value):
  """
  Checks if assigning a value to a square maintains row and column sums.
  """
  target_sum = 36
  return (calculate_row_sum(board, row) + value <= target_sum and
          calculate_col_sum(board, col) + value <= target_sum)

def solve_knight_tour(board, row=0, col=0):
  """
  Solves the Knight's tour problem using backtracking with probabilistic move selection.
  """
  # Base case: All squares are filled
  if row == 7 and col == 7:
    return True

  # Get valid moves for current position
  valid_moves = get_valid_moves(board, row, col)

  # Check if no valid moves exist - dead end
  if not valid_moves:
    return False

  # Randomly shuffle valid moves to introduce some randomness
  random.shuffle(valid_moves)

  # Try all valid moves
  for next_row, next_col in valid_moves:
    # Find possible values that satisfy row and column sums
    possible_values = [i for i in range(1, 65) if is_valid_assignment(board, next_row, next_col, i)]

    # Backtrack for each possible value
    for value in possible_values:
      board[next_row][next_col] = value
      if solve_knight_tour(board, next_row, next_col):
        return True
      board[next_row][next_col] = -1  # Backtrack

  return False

def main():
  """
  Reads input, solves the Knight's tour, and prints the output.
  """
  board = []
  for _ in range(8):
    row = [int(x) for x in input().split()]
    board.append(row)

  if solve_knight_tour(board):
    for row in board:
      print(*row, sep=" ")
  else:
    print("No solution found")

if __name__ == "__main__":
  main()
