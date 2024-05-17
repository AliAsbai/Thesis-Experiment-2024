#! /usr/bin/python3

class Square:
  def __init__(self, row, col, symbol):
    self.row = row
    self.col = col
    self.symbol = symbol
    self.visited = False

def is_valid(board, row, col):
  return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col].symbol != 'K'

def get_neighbors(board, row, col):
  neighbors = []
  # Check normal movements (up, down, left, right)
  for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    new_row, new_col = row + dr, col + dc
    if is_valid(board, new_row, new_col):
      neighbors.append(board[new_row][new_col])
  # Check knight-like jumps ('K' tiles) centered on current square
  for dr, dc in [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]:
    new_row, new_col = row + dr, col + dc
    if is_valid(board, new_row, new_col) and board[row][col].symbol != 'R':  # Don't jump from starting square (marked 'R')
      neighbors.append(board[new_row][new_col])
      board[new_row][new_col].visited = False  # Mark neighbors as not visited (important fix)
  return neighbors

def bfs(board, start_row, start_col, target_row, target_col):
  queue = [(start_row, start_col)]  # Use tuple for coordinates
  visited = set()  # Use set for faster membership checks

  while queue:
    current_row, current_col = queue.pop(0)
    if (current_row, current_col) in visited:
      continue  # Skip already visited squares
    visited.add((current_row, current_col))  # Mark current square as visited

    if current_row == target_row and current_col == target_col:
      return True
    for neighbor in get_neighbors(board, current_row, current_col):
      queue.append((neighbor.row, neighbor.col))
  return False

if __name__ == "__main__":
  rows, cols = map(int, input().split())
  board = []
  for _ in range(rows):
    row = [Square(i, j, char) for j, char in enumerate(input())]
    board.append(row)

  start_row, start_col = None, None
  target_row, target_col = None, None
  for i in range(rows):
    for j in range(cols):
      if board[i][j].symbol == 'R':
        start_row, start_col = i, j
      elif board[i][j].symbol == 'T':
        target_row, target_col = i, j
  
  if bfs(board, start_row, start_col, target_row, target_col):
    print("yes")
  else:
    print("no")
