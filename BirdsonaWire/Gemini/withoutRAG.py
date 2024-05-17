def max_additional_birds(length, distance, occupied_positions):
  """
  Calculates the maximum number of additional birds that can sit on the wire.

  Args:
      length: The length of the wire in centimeters (1 <= length <= 1000000000).
      distance: The minimum distance between birds in centimeters (1 <= distance <= 1000000000).
      occupied_positions: A list of integers representing the positions of occupied spots (0 <= len(occupied_positions) <= 20000).

  Returns:
      An integer representing the maximum number of additional birds.
  """

  # Input validation (optional, but recommended for robustness)
  if not (1 <= length <= 1000000000):
    raise ValueError("Invalid wire length. Must be between 1 and 1 billion centimeters.")
  if not (1 <= distance <= 1000000000):
    raise ValueError("Invalid minimum bird distance. Must be between 1 and 1 billion centimeters.")
  if not (0 <= len(occupied_positions) <= 20000):
    raise ValueError("Invalid number of birds. Must be between 0 and 20,000.")

  # Sort occupied positions for efficient gap calculation
  occupied_positions.sort()

  # Define first and last valid positions for birds (excluding poles)
  first_valid = distance + 6
  last_valid = length - distance - 6

  # Handle edge cases: empty wire
  if not occupied_positions:
    return (last_valid - first_valid) // distance + 1

  # Edge cases: single bird at the beginning/end (handled iteratively)
  while occupied_positions[0] == first_valid:
    occupied_positions.pop(0)
    if not occupied_positions:
      return (last_valid - first_valid) // distance + 1
  while occupied_positions[-1] == last_valid:
    occupied_positions.pop()

  # Calculate gaps between birds and poles
  gaps = [first_valid - occupied_positions[0]] + [occupied_positions[i] - occupied_positions[i - 1] - distance for i in range(1, len(occupied_positions))] + [last_valid - occupied_positions[-1]]

  # Find the largest gap to fit a bird
  max_gap = max(gaps)

  # Calculate the number of birds that can fit in the largest gap
  return max_gap // distance

# Read input data
try:
  length, distance, num_birds = map(int, input().split())
  occupied_positions = []
  for _ in range(num_birds):
    occupied_positions.append(int(input()))
except ValueError as e:
  print("Error:", e)
  exit()  # Terminate program on invalid input

# Calculate and print the result
additional_birds = max_additional_birds(length, distance, occupied_positions)
print(additional_birds)
