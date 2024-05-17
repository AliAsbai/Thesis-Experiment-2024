#! /usr/bin/python3

def max_guests(apartment):
  """
  Finds the maximum number of guests Mirko can invite for dinner.

  Args:
      apartment: A list of strings representing the layout of the apartment.

  Returns:
      The maximum number of guests Mirko can invite.
  """
  rows, cols = len(apartment), len(apartment[0])
  dp = [[0] * cols for _ in range(rows)]

  # Preprocess the apartment layout to store cumulative free space
  for row in range(rows):
    for col in range(cols):
      if apartment[row][col] == '.':
        dp[row][col] = (dp[row][col - 1] if col > 0 else 0) + 1
      else:
        dp[row][col] = 0

  # Find the maximum perimeter (guests) for all table heights
  max_guests = 0
  for height in range(1, 1001):
    length = 0  # Track table length along the current row
    for row in range(rows):
      for col in range(cols):
        if dp[row][col] >= height:
          length += 1
        else:
          length = 0
      # Consider table corners: add height for each usable row/column
      # Adjust for double counting corners in square tables
      corner_bonus = (rows - 1 if length == cols else 0) + (cols - 1 if all(dp[row][col] >= height for col in range(cols)) else 0)
      max_guests = max(max_guests, 2 * (length + height) + corner_bonus - (height - 1 if length == height else 0))

  return max_guests

# Read input
rows, cols = map(int, input().split())
apartment = [input() for _ in range(rows)]

# Find and print the maximum number of guests
print(max_guests(apartment))
