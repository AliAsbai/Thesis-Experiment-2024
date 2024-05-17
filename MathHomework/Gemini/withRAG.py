#! /usr/bin/python3

def count_seat_adjustments(preferences, policy):
  """Counts the number of seat adjustments required for a given policy.

  Args:
      preferences: A list of integers representing seat preferences (1 for 'U', 0 for 'D').
      policy: An integer representing the policy (1, 2, or 3).

  Returns:
      An integer representing the number of seat adjustments required.
  """
  seat_position = preferences[0]
  adjustments = 0

  for pref in preferences[1:]:
    if pref != seat_position:
      adjustments += 1
      seat_position = pref

  # Add adjustments for leaving the seat according to policy
  if policy == 1 and seat_position == 0:
    adjustments += 1
  elif policy == 2 and seat_position == 1:
    adjustments += 1
  elif policy == 3:
    pass  # No adjustment needed for policy 3 when leaving

  return adjustments

def main():
  """Reads input, converts to preferences list, calculates adjustments for each policy, and prints results."""
  preferences = [int(x) for x in input().split()]  # Convert input string to list of integers
  policy1_adjustments = count_seat_adjustments(preferences, 1)
  policy2_adjustments = count_seat_adjustments(preferences, 2)
  policy3_adjustments = count_seat_adjustments(preferences, 3)

  print(policy1_adjustments)
  print(policy2_adjustments)
  print(policy3_adjustments)

if __name__ == "__main__":
  main()
