def count_winning_instances(board, magic_number, starting_position):
  """
  Counts the number of winning instances for a given Frogger board configuration.

  Args:
      board: A list of integers representing the board squares.
      magic_number: The integer the frog needs to reach to win.
      starting_position: The index of the square the frog starts on (1-indexed).

  Returns:
      The number of winning instances for this starting position and magic number.
  """
  n = len(board)
  visited = set()  # Track visited squares to detect cycles

  def dfs(current_position, max_hops=n):
    """
    Depth-First Search to explore possible paths and count wins.

    Args:
        current_position: The index of the current square the frog is on.
        max_hops: Maximum allowed hops to prevent infinite loops (optional).

    Returns:
        The number of winning instances reachable from the current position.
    """

    if max_hops <= 0:
      # Maximum hop limit reached, potential infinite loop (return 0 wins)
      return 0

    if current_position <= 0 or current_position > n:
      # Frog falls off the board, losing condition (return 0 wins)
      return 0

    if board[current_position - 1] == magic_number:
      # Frog reaches the magic number, winning condition (return 1 win)
      return 1

    if current_position in visited:
      # Cycle detected, no further exploration needed (return 0 wins)
      return 0

    visited.add(current_position)

    hop = abs(board[current_position - 1])
    next_position = current_position + hop if board[current_position - 1] > 0 else current_position - hop

    # Explore both forward and backward hops (if applicable)
    wins = dfs(next_position, max_hops-1)  # Recursive call with reduced max_hops

    visited.remove(current_position)  # Backtrack after exploring path

    return wins  # Return the number of wins from the explored path

  # Input Validation (optional)
  if n < 1 or n > 200000 or any(num == 0 for num in board):
    raise ValueError("Invalid board configuration")

  # Start exploration from the starting position
  return dfs(starting_position)

# Read input
try:
  n = int(input())
  board = list(map(int, input().split()))
except ValueError:
  print("Invalid input format")
  exit()

# Initialize total winning instances
total_winning_instances = 0

# Check for each starting position and each possible magic number
for starting_position in range(1, n + 1):
  for magic_number in set(board):
    total_winning_instances += count_winning_instances(board, magic_number, starting_position)

# Print total winning instances
print(total_winning_instances)
