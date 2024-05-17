#! /usr/bin/python3

def min_shelves(small, medium, large, shelf_width):
  """
  Calculates the minimum number of shelves needed to fit all books.

  Args:
      small: Number of small books (width 1).
      medium: Number of medium books (width 2).
      large: Number of medium books (width 3).
      shelf_width: Width of a single shelf.

  Returns:
      The minimum number of shelves needed.
  """
  # Minimum shelves needed considering all books fit on one shelf each
  min_shelves = max(small // shelf_width, medium, large // (shelf_width // 3))

  # Fill remaining width with small and medium books (not applicable here)
  # remaining_width = shelf_width % 3  # No need to calculate remaining space

  # No need for the loop as all books are placed in min_shelves calculation

  return min_shelves

# Read input
small, medium, large = map(int, input().split())
shelf_width = int(input())

# Calculate and print minimum shelves
print(min_shelves(small, medium, large, shelf_width))
