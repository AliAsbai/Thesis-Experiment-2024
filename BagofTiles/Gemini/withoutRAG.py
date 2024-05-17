from collections import Counter

def calculate_odds(tiles, n, target):
  """
  Calculates the odds of winning the game given the tiles, number of tiles to draw, and target sum.

  Args:
      tiles: A list of integers representing the tile values.
      n: An integer representing the number of tiles to draw.
      target: An integer representing the target sum.

  Returns:
      A tuple containing the number of winning draws and total possible draws.
  """

  # Count occurrences of each tile value
  tile_counts = Counter(tiles)

  # Early check to avoid unnecessary calculations (if target unreachable)
  if any(target - i * val < 0 for i, val in tile_counts.items()):
    return 0, len(tiles)**n  # No winning combinations

  # Use dynamic programming for efficient calculation
  dp = [[0] * (target + 1) for _ in range(n + 1)]

  # Initialize base cases (1 tile, sum = 0)
  for i in range(len(tiles) + 1):
    dp[i][0] = 1  # 1 way to achieve sum 0 with any number of tiles

  for i in range(1, n + 1):  # Number of tiles to draw
    for j in range(1, target + 1):  # Target sum
      for tile, count in tile_counts.items():
        if tile <= j and count >= i:  # Ensure tile fits sum and enough copies
          # Use combinations from previous states (i-1 tiles) with remaining sum
          dp[i][j] += dp[i - 1][j - tile]

  winning_draws = dp[n][target]
  total_draws = len(tiles)**n

  return winning_draws, total_draws

def main():
  """
  Reads the input, calculates odds for each game, and prints the results.
  """
  num_games = int(input())
  for game_num in range(1, num_games + 1):
    try:
      num_tiles = int(input())
      tiles = list(map(int, input().split()))
      n, target = map(int, input().split())
      winning_draws, total_draws = calculate_odds(tiles, n, target)
      print(f"Game {game_num} -- {winning_draws} : {total_draws}")
    except ValueError:
      print(f"Game {game_num} -- Invalid Input")  # Handle potential input errors

if __name__ == "__main__":
  main()
