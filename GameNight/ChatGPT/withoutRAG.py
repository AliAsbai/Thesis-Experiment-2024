def min_seat_changes(n, teams):
    team_counts = {'A': 0, 'B': 0, 'C': 0}
    total_changes = 0

    # Count the initial occurrences of each team
    for team in teams:
        team_counts[team] += 1

    # Initialize a sliding window of length n
    window_start = 0
    min_changes = float('inf')

    for window_end in range(n):
        team_counts[teams[window_end]] -= 1  # Remove the team at window_end from the window
        total_changes += 1  # Increment the total changes needed

        # Shrink the window until all teams are adjacent
        while all(count <= 0 for count in team_counts.values()):
            min_changes = min(min_changes, total_changes)  # Update the minimum changes needed
            team_counts[teams[window_start]] += 1  # Restore the team at window_start
            total_changes -= 1  # Decrement the total changes needed
            window_start += 1  # Slide the window

    return min_changes

# Sample Input
n = 5
teams = "ABABC"

# Output
print(min_seat_changes(n, teams))
