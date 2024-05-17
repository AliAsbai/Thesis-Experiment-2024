def max_guests(apartment):
  """
  This function finds the number of guests Mirko can invite for dinner 
  based on the layout of his apartment, considering all valid placements.

  Args:
      apartment: A list of strings representing the layout of the apartment.

  Returns:
      The maximum number of guests Mirko can invite.
  """
  rows, cols = len(apartment), len(apartment[0])
  max_perimeter = 0

  for row in range(rows):
    # Track consecutive free squares considering edge cases
    left_free, right_free = 0, 0
    for col in range(cols):
      if apartment[row][col] == '.':
        left_free += 1
        right_free = cols - col if col == cols - 1 else right_free + 1
      else:
        left_free = right_free = 0
      # Consider valid placements (including edge cases)
      max_perimeter = max(max_perimeter, 2 * (min(left_free, right_free) + 1))

  for col in range(cols):
    # Track consecutive free squares for columns and consider edge cases
    top_free, bottom_free = 0, 0
    for row in range(rows):
      if apartment[row][col] == '.':
        top_free += 1
        bottom_free = rows - row if row == rows - 1 else bottom_free + 1
      else:
        top_free = bottom_free = 0
      # Consider valid placements (including edge cases)
      max_perimeter = max(max_perimeter, 2 * (min(top_free, bottom_free) + 1))

  return max_perimeter

# Read input
rows, cols = map(int, input().split())
apartment = [input() for _ in range(rows)]

# Find the maximum number of guests
max_guests_count = max_guests(apartment)

# Print output
print(max_guests_count)
