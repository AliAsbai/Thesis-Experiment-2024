#! /usr/bin/python3

def solve_team(data):
  """
  This function takes a list of 5 integers representing team data 
  (games played, wins, draws, losses, points) and fills in missing values.

  Args:
      data: A list containing team data.

  Returns:
      A list with the missing values filled in, or None if no solution exists.
  """
  known_count = sum(val != "?" for val in data)
  if known_count == 5:
    # All values known, check consistency
    return data if data[4] == sum(data[i] for i in range(1, 4)) else None
  elif known_count == 4:
    # Try to solve for one missing value based on known relationships
    for i in range(5):
      if data[i] == "?":
        other_sum = sum(data[j] for j in range(5) if j != i)
        if (i == 0 and other_sum <= 100) or (i == 4 and other_sum >= 0):
          data[i] = (other_sum - data[1] - data[2] - data[3]) if i != 4 else data[0] - sum(data[j] for j in range(1, 4))
          if data[i] >= 0:
            return data
    return None
  else:
    # Handle cases with multiple unknowns
    if data[0] == "?":  # Total games unknown
      return None
    elif data[1] == "?" and data[2] == "?":  # Both wins and draws unknown
      # Points known, calculate possible wins considering non-divisible points
      max_wins = data[4] // 3
      for wins in range(max_wins + 1):
        remaining_points = data[4] - 3 * wins
        if remaining_points >= 0 and remaining_points % 2 == 0:  # Points remaining must be even (draws give 1 point)
          draws = remaining_points // 2
          losses = data[0] - wins - draws
          if losses >= 0:
            data[1] = wins
            data[2] = draws
            data[3] = losses
            return data
      return None
    else:  # One of wins or draws unknown, calculate the other
      # Prioritize known value (wins if known, draws if known)
      known_val, unknown_val = (data[1], data[2]) if data[1] != "?" else (data[2], data[1])
      # Calculate remaining points and losses based on known value
      remaining_points = data[4] - 3 * known_val
      losses = data[0] - known_val - (remaining_points // 2)  # Losses based on half of remaining points (draws)
      # Check if remaining points are even and losses are valid
      if remaining_points % 2 == 0 and losses >= 0:
        # Valid solution found, assign values
        data[unknown_val] = remaining_points // 2
        data[3] = losses
        return data
      # If not valid, check with remaining points being odd (all draws)
      if remaining_points >= 1 and (remaining_points - 1) % 2 == 0 and losses - 1 >= 0:
        # Valid solution with all draws, assign values
        data[unknown_val] = (remaining_points - 1) // 2
        data[3] = losses - 1
        return data
      return None


def main():
  """
  This function reads input, solves for each team, and prints the results.
  """
  num_teams = int(input())
  for _ in range(num_teams):
    team_data = [int(val) if val != "?" else val for val in input().split()]
    result = solve_team(team_data.copy())
    if result:
      print(*result)
    else:
      print("??" * 5)

if __name__ == "__main__":
  main()
