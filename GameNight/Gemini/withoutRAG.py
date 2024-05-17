def min_seat_switches(arrangement):
  """
  Calculates the minimum number of people who need to switch seats
  for teams to sit together at a circular table.

  Args:
      arrangement: A string representing the teams of people (A, B or C).

  Returns:
      An integer representing the minimum number of seat switches.
  """
  n = len(arrangement)
  
  # Count occurrences of each team
  team_counts = {'A': 0, 'B': 0, 'C': 0}
  for char in arrangement:
    team_counts[char] += 1

  # Find the team with the largest difference from ideal size
  ideal_size = n // len(team_counts)
  max_diff_team = max(team_counts, key=lambda team: abs(team_counts[team] - ideal_size))
  max_diff = abs(team_counts[max_diff_team] - ideal_size)
  
  # Handle cases where only one person needs to switch
  if max_diff == 1:
    return 1
  
  # Calculate minimum switches based on largest difference
  return max_diff

# Read input
n = int(input())
arrangement = input()

# Calculate and print minimum switches
min_switches = min_seat_switches(arrangement)
print(min_switches)
