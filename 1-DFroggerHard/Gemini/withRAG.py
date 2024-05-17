#! /usr/bin/python3

def dfs(board, magic_num, curr_pos, visited, winning_instances):
  """
  Performs a depth-first search to explore possible game paths.

  Args:
      board: List of integers representing the board squares.
      magic_num: The magic number for this game instance.
      curr_pos: The current position of the frog.
      visited: Set to track visited squares and avoid cycles.
      winning_instances: Counter to keep track of winning instances.
  """
  # Check for win condition (landing on magic number)
  if board[curr_pos - 1] == magic_num:
    winning_instances.append(1)
    return

  # Check for losing conditions (falling off or cycle)
  if curr_pos <= 0 or curr_pos > len(board) or curr_pos in visited:
    return

  # Mark current position as visited
  visited.add(curr_pos)

  # Explore next hop based on board value
  hop_distance = abs(board[curr_pos - 1])
  next_pos = curr_pos + hop_distance if board[curr_pos - 1] > 0 else curr_pos - hop_distance

  # Perform DFS on the next position
  dfs(board, magic_num, next_pos, visited.copy(), winning_instances)

def main():
  """
  Reads input, parses board and magic number, and calls DFS to count winning instances.
  """
  n = int(input())
  board_str = input()  # Read the entire line for board squares
  board = list(map(int, board_str.split()))  # Split on spaces

  magic_num = int(input())

  winning_instances = []
  visited = set()

  # Start DFS from each starting position
  for i in range(1, n + 1):
    dfs(board, magic_num, i, visited, winning_instances)

  # Print the total number of winning instances
  print(sum(winning_instances))

if __name__ == "__main__":
  main()
