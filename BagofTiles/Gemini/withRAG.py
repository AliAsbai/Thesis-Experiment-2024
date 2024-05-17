#! /usr/bin/python3

import sys

def factorial(n):
  """Calculates the factorial of a number."""
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def count_winning_combinations(tiles, target, num_draw):
  """
  Counts the number of winning combinations for a specific draw.

  Args:
      tiles: List of integers representing tile values.
      target: Integer representing the target sum.
      num_draw: Integer representing the number of tiles to draw.

  Returns:
      Integer representing the number of winning combinations.
  """
  # Calculate total possible combinations.
  total_combinations = factorial(len(tiles)) // factorial(len(tiles) - num_draw) // factorial(num_draw)

  # Special case for target sum of 0.
  if target == 0:
    # Winning combination only occurs when no tiles are drawn.
    return 1 if num_draw == 0 else 0

  # Check if all tiles have the same value.
  all_same = all(tile == tiles[0] for tile in tiles[1:])

  # Winning combinations are not possible if all tiles are the same and target doesn't match a multiple of the tile value.
  if all_same and target % tiles[0] != 0:
    return 0

  # Special case for target equal to the value of one tile.
  if target in tiles:
    # Count of winning combinations where the target tile is drawn at least once.
    winning_combinations_with_target = total_combinations - count_winning_combinations(tiles, target - target, num_draw - 1)
  else:
    winning_combinations_with_target = 0

  # Count of winning combinations where the target tile is not drawn.
  winning_combinations_without_target = count_winning_combinations([tile for tile in tiles if tile != target], target, num_draw)

  # Combine winning combinations from both cases.
  return winning_combinations_with_target + winning_combinations_without_target

def main():
  """Reads input, calculates odds, and prints results."""
  for line in sys.stdin:
    num_games = int(line)
    for _ in range(num_games):
      # Read game data.
      num_tiles = int(sys.stdin.readline())
      tiles = list(map(int, sys.stdin.readline().split()))
      num_draw, target = map(int, sys.stdin.readline().split())

      # Calculate winning combinations and total combinations.
      winning_combinations = count_winning_combinations(tiles, target, num_draw)
      total_combinations = 2**num_tiles

      # Print results.
      print(f"Game {_ + 1} -- {winning_combinations} : {total_combinations - winning_combinations}")

if __name__ == "__main__":
  main()
