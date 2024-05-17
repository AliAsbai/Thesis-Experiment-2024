def seat_adjustments(preferences):
  """
  Calculates the number of seat adjustments required for each policy.

  Args:
      preferences: A string of characters 'U' and 'D' indicating seat preferences.

  Returns:
      A tuple containing the number of adjustments for each policy (Up, Down, As-Is).
  """
  current_seat = preferences[0]  # Initial seat position
  up_adjustments = down_adjustments = as_is_adjustments = 0

  for pref in preferences[1:]:
    if pref != current_seat:
      # Need adjustment (excluding last person)
      if pref == 'U':
        up_adjustments += 1
      else:
        down_adjustments += 1
      current_seat = pref

  # Only the last person adjusts for As-Is policy
  if current_seat != preferences[-1]:
    as_is_adjustments += 1  

  # Everyone adjusts before leaving (except initial seat matches preference)
  if current_seat != preferences[0]:
    up_adjustments += 1
    down_adjustments += 1

  return up_adjustments, down_adjustments, as_is_adjustments

# Read preferences from input (handle potential errors)
try:
  preferences = input()
except EOFError:
  print("Error: No input received.")
  exit(1)

# Validate input length
if len(preferences) < 2 or len(preferences) > 1000:
  print("Error: Invalid input length. String must be between 2 and 1000 characters.")
  exit(1)

# Ensure characters are valid
if not all(char in ('U', 'D') for char in preferences):
  print("Error: Invalid characters in input. Only 'U' and 'D' allowed.")
  exit(1)

# Calculate adjustments for each policy
up_adjustments, down_adjustments, as_is_adjustments = seat_adjustments(preferences)

# Print results
print(up_adjustments)
print(down_adjustments)
print(as_is_adjustments)

# Example usage
preferences = "UUUDDUDU"
seat_adjustments(preferences)
