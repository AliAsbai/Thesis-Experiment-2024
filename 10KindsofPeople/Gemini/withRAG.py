#! /usr/bin/python3

def is_valid(grid, r, c):
  """Checks if coordinates are within grid bounds."""
  return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def can_move(grid, r1, c1, r2, c2):
  """
  Checks if movement is possible based on user type and original value connectivity.
  """
  return "neither" if grid[r1-1][c1-1] != grid[r2-1][c2-1] else ("binary" if grid[r1-1][c1-1] == "0" else "decimal")

# Read input data
rows, cols = map(int, input().split())
grid = []
for _ in range(rows):
  grid.append(list(input()))

# Read and process queries
queries = int(input())
for _ in range(queries):
  r1, c1, r2, c2 = map(int, input().split())
  print(can_move(grid, r1, c1, r2, c2))
