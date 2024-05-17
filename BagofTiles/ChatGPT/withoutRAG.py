from itertools import combinations

# Function to calculate the odds of winning for a single game
def calculate_odds(tiles, n, t):
    # Count the number of winning and losing combinations
    win_count = sum(1 for draw in combinations(tiles, n) if sum(draw) == t)
    total_possible_draws = len(list(combinations(tiles, n)))
    loss_count = total_possible_draws - win_count
    return win_count, loss_count

# Main function to read input and output results
def main():
    g = int(input())  # Number of games
    for game in range(g):
        m = int(input())  # Number of tiles in the bag
        tiles = list(map(int, input().split()))  # Tiles in the bag
        n, t = map(int, input().split())  # Values of n and t
        wins, losses = calculate_odds(tiles, n, t)
        print(f"Game {game + 1} -- {wins} : {losses}")

if __name__ == "__main__":
    main()
