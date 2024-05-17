import sys

def solve_team_stats(team_stats):
    # Extracting team statistics
    games_played, games_won, games_drawn, games_lost, points_earned = team_stats

    # Convert '?' to None for easier processing
    team_stats = [int(val) if val != '?' else None for val in team_stats]

    # Count the number of unknowns
    unknowns = team_stats.count(None)

    # If all values are known, return the stats as is
    if unknowns == 0:
        return team_stats

    # If there's only one unknown, fill it based on the known values
    if unknowns == 1:
        if games_played is not None and games_won is not None and games_drawn is not None and games_lost is not None:
            points_earned = games_won * 3 + games_drawn
            return [games_played, games_won, games_drawn, games_lost, points_earned]
        elif games_played is not None and games_won is not None and games_drawn is not None and points_earned is not None:
            games_lost = points_earned - games_won * 3 - games_drawn
            return [games_played, games_won, games_drawn, games_lost, points_earned]
        elif games_played is not None and games_won is not None and games_lost is not None and points_earned is not None:
            games_drawn = points_earned - games_won * 3 - points_earned
            return [games_played, games_won, games_drawn, games_lost, points_earned]
        elif games_played is not None and games_drawn is not None and games_lost is not None and points_earned is not None:
            games_won = (points_earned - games_drawn - games_lost) / 3
            return [games_played, games_won, games_drawn, games_lost, points_earned]

    # If there are two unknowns, solve them based on the known values
    if unknowns == 2:
        if games_played is None:
            games_played = games_won + games_drawn + games_lost
        elif games_won is None:
            games_won = (points_earned - games_drawn) // 3
        elif games_drawn is None:
            games_drawn = points_earned - (games_won * 3) - games_lost
        elif games_lost is None:
            games_lost = games_played - games_won - games_drawn

    # Calculate points earned
    points_earned = games_won * 3 + games_drawn

    # Convert None back to '?' for output
    return [val if val is not None else '?' for val in [games_played, games_won, games_drawn, games_lost, points_earned]]

def main():
    # Read number of teams
    num_teams = int(input())

    # Iterate over teams
    for _ in range(num_teams):
        team_stats = input().split()
        # Solve team statistics
        solved_stats = solve_team_stats(team_stats)
        # Print the solved statistics
        print(' '.join(map(str, solved_stats)))

if __name__ == "__main__":
    main()
