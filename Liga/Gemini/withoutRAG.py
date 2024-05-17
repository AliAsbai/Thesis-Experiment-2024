def calculate_missing_stats(team_data):
  """
  Calculates missing statistics for a given team's data, handling invalid input and edge cases.

  Args:
      team_data: A list containing 5 integers or '?' representing games played, wins, draws, losses, and points.

  Returns:
      A list with all fields filled with calculated values (or the original '?' if no valid calculation exists).
  """
  games_played, wins, draws, losses, points = team_data

  # Check for invalid points (not a multiple of 3 with maximum possible draws)
  if points != '?' and (points % 3) > (games_played - wins):
    return team_data  # Points can't be higher than possible draws

  # Check for at least one known field to calculate games played
  if games_played == '?' and all(field == '?' for field in [wins, draws, losses]):
    return team_data  # Can't calculate games played without any known data

  # Calculate games played if unknown (assuming valid data)
  if games_played == '?':
    games_played = wins + draws + losses

  # Calculate missing fields based on known values and game theory rules, handling invalid cases

  # Wins calculation
  if wins == '?':
    # Ensure points are valid (multiple of 3 + draws) before calculating wins
    if points != '?' and (points % 3) != draws:
      return team_data  # Invalid points, can't calculate wins
    wins = (points - (draws)) // 3
  # Draws calculation (consider negative remainder for invalid points)
  elif draws == '?':
    if points != '?' and abs(points % 3) > draws:  # Absolute value to handle negative remainders
      return team_data
    draws = points % 3
  # Losses calculation
  elif losses == '?':
    losses = games_played - wins - draws
  # Points calculation
  elif points == '?':
    points = (wins * 3) + draws

  return [games_played, wins, draws, losses, points]

def main():
  """
  Reads input, calculates missing stats, and prints the complete table (or original data if calculation fails).
  """
  num_teams = int(input())

  for _ in range(num_teams):
    team_data = input().split()
    completed_data = calculate_missing_stats(team_data)
    print(*completed_data)

if __name__ == "__main__":
  main()
