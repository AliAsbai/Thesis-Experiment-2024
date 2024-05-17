def min_tower_height(h0):
  """
  Calculates the minimum height for a house of cards with equal suits.

  Args:
      h0: The minimum desired height of the tower.

  Returns:
      The smallest possible height h such that the tower can be built.
  """
  # Each card layer requires 4 cards (one for each suit).
  cards_per_layer = 4

  # Initialize with the minimum desired height.
  h = h0

  # Loop with modulo operation to avoid overflow for large inputs.
  while (h % cards_per_layer) != 1:
    h += 1

  return h

# Get user input for minimum desired height.
try:
  h0 = int(input("Enter the minimum desired height (1-10^1000): "))

  # Validate input
  if h0 < 1 or h0 > 10**1000:
    raise ValueError("Invalid input: Height must be between 1 and 10^1000.")

  # Calculate minimum possible height.
  min_height = min_tower_height(h0)

  # Print the result.
  print(f"Minimum possible height for equal suit distribution: {min_height}")

except ValueError as e:
  print("Error:", e)
