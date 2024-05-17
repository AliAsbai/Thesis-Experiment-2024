#! /usr/bin/python3

def min_height(h0):
  """
  Calculates the smallest possible height for the house of cards.

  Args:
      h0: Minimum desired height of the house.

  Returns:
      The smallest possible height for the house of cards.
  """
  h = h0
  while h * (h + 1) < h0 * 4:
    h += 1
  return h

# Read input from STDIN
h0 = int(input())

# Calculate and print the smallest possible height
print(min_height(h0))
