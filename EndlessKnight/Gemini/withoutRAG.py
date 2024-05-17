MOD = 10007

def is_valid(board, row, col, rocks):
  """Checks if the knight can move to a square, considering restrictions."""
  if 1 <= row <= len(board) and 1 <= col <= len(board[0]) and (row, col) not in rocks:
    return row > 1 or col > 1  # Cannot move to the top-left square again
  return False

def dp_solve(H, W, R, rocks):
  """Solves Knight's tour using Dynamic Programming."""
  dp = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
  dp[1][1] = 1  # Starting square has 1 option

  for row in range(1, H + 1):
    for col in range(1, W + 1):
      if is_valid(board, row, col, rocks):
        # Check for out-of-bounds access before using values from previous rows
        prev_row1, prev_col1 = row - 2, col - 1
        prev_row2, prev_col2 = row - 1, col - 2
        count = 0
        if 1 <= prev_row1 <= H and 1 <= prev_col1 <= W:
          count += dp[prev_row1][prev_col1]
        if 1 <= prev_row2 <= H and 1 <= prev_col2 <= W:
          count += dp[prev_row2][prev_col2]
        dp[row][col] = count % MOD

  return dp[H][W]

def main():
  """Reads input and prints results."""
  T = int(input())
  for case in range(1, T + 1):
    H, W, R = map(int, input().split())
    rocks = set([(int(r), int(c)) for r, c in [input().split() for _ in range(R)]])
    result = dp_solve(H, W, R, rocks)
    print(f"Case #{case}: {result}")

if __name__ == "__main__":
  main()
