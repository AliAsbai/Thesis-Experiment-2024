def can_reach(grid, r1, c1, r2, c2, user_type):
  """
  Checks if a user of the specified type can reach the destination from the source in the binary-decimal map.

  Args:
      grid: A 2D list representing the map (0s for binary, 1s for decimal)
      r1: Starting row coordinate (1-based)
      c1: Starting column coordinate (1-based)
      r2: Destination row coordinate (1-based)
      c2: Destination column coordinate (1-based)
      user_type: "binary" or "decimal" depending on the user type

  Returns:
      "binary" if a binary user can reach, "decimal" if a decimal user can reach, or "neither" otherwise
  """

  rows, cols = len(grid), len(grid[0])  # Get grid dimensions
  visited = [[False for _ in range(cols)] for _ in range(rows)]  # Visited cell tracker
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movement options

  def dfs(row, col):
    # Base cases
    if row == r2 and col == c2:  # Reached destination, return user type
      return user_type
    if visited[row - 1][col - 1] or grid[row - 1][col - 1] != (user_type == "binary"):
      # Visited cell or restricted cell for user type
      return "neither"

    visited[row - 1][col - 1] = True  # Mark cell as visited
    for dx, dy in directions:
      new_row, new_col = row + dx, col + dy
      if 0 <= new_row < rows and 0 <= new_col < cols:  # Check boundaries
        # Check if the new cell is within grid and not visited
        result = dfs(new_row, new_col)
        if result != "neither":  # Found a valid path from this direction
          return result
    return "neither"  # No valid path found from any direction

  # Convert 1-based coordinates to 0-based for indexing
  result = dfs(r1 - 1, c1 - 1)
  return result if result != "neither" else "neither"

# Read input (ensure correct format)
rows, cols = map(int, input().split())
grid = [list(map(int, input())) for _ in range(rows)]
num_queries = int(input())

# Process queries
for _ in range(num_queries):
  r1, c1, r2, c2 = map(int, input().split())
  user_type = "binary" if grid[r1 - 1][c1 - 1] == 0 else "decimal"
  result = can_
