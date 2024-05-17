def calculate_missing_fields(team):
    total_games, wins, draws, losses, points = team

    # Calculate missing fields if they exist
    if '?' in team:
        missing_index = team.index('?')

        if missing_index == 0:  # Total games
            total_games = wins + draws + losses
        elif missing_index == 1:  # Wins
            wins = (points - draws - losses * 3) // 3
        elif missing_index == 2:  # Draws
            draws = (points - wins * 3 - losses) // 1
        elif missing_index == 3:  # Losses
            losses = (points - wins * 3 - draws) // 3
        else:  # Points
            points = wins * 3 + draws

    return total_games, wins, draws, losses, points


# Read input
N = int(input())  # Number of teams
teams_data = [list(input().split()) for _ in range(N)]

# Fill missing fields and print output
for team in teams_data:
    filled_team = calculate_missing_fields(team)
    print(*filled_team)
