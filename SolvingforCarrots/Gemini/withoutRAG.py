def count_carrots(contestants, huffle_puffs):
  """
  This function calculates the total number of carrots awarded in a contest.

  Args:
      contestants: An integer representing the number of contestants.
      huffle_puffs: An integer representing the total number of huffle-puff problems solved.

  Returns:
      An integer representing the total number of carrots awarded.
  """
  carrots = huffle_puffs  # Base carrots for huffle-puff problems

  # Check if any contestant description implies solving huffle-puff problems
  for contestant in range(contestants):
    description = input()
    if "huckle" in description.lower() or "problem" in description.lower():
      carrots += 1  # Award carrot for solving huffle-puff problems based on description

  return carrots

# Read input for number of contestants and huffle-puff problems
contestants, huffle_puffs = map(int, input().split())

# Calculate total carrots and print the result
total_carrots = count_carrots(contestants, huffle_puffs)
print(total_carrots)
