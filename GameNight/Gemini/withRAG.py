#! /usr/bin/python3

def min_moves(string):
  """
  Calculates the minimum number of people who need to switch seats 
  to ensure teams sit together.

  Args:
      string: A string of characters 'A', 'B', 'C' representing teams.

  Returns:
      The minimum number of people who need to switch seats.
  """
  n = len(string)
  # Count occurrences of each character (team)
  char_count = {'A': 0, 'B': 0, 'C': 0}
  for char in string:
    char_count[char] += 1

  # Create a 2D vector to store prefix sums of each character type
  prefix = [[0, 0, 0] for _ in range(n)]
  prefix[0][ord(string[0]) - ord('A')] = 1
  for i in range(1, n):
    for j in range(3):
      prefix[i][j] = prefix[i-1][j] + (j == ord(string[i]) - ord('A'))

  # Iterate through possible starting positions for each team (A, B, C)
  min_moves = float('inf')
  for start in range(n):
    moves = 0
    # Calculate moves needed for characters to be in their desired positions
    for i in range(start, n):
      char = string[i]
      desired_pos = (i - start) % char_count[char]
      # Avoid counting moves when a character is already in its desired position
      if i != start + desired_pos:
        moves += abs(prefix[i][ord(char) - ord('A')] - prefix[start-1][ord(char) - ord('A')] - (desired_pos + 1))

    # Calculate moves needed for characters outside to be moved away
    for i in range(start):
      char = string[i]
      undesired_pos = (i - start) % char_count[char]
      moves += prefix[n-1][ord(char) - ord('A')] - prefix[i][ord(char) - ord('A')] - undesired_pos

    min_moves = min(min_moves, moves)

  return min_moves

if __name__ == "__main__":
  for line in sys.stdin:
    n = int(line)
    string = sys.stdin.readline().strip()
    print(min_moves(string))
