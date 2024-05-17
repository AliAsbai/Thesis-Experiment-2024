import sys
from itertools import combinations

def calculate_odds(m, tiles, n, t):
    if n == 0:
        # If n is zero, only one combination is possible: choosing zero tiles
        return 1, m ** n - 1 if m > 0 else 0
    
    total_combinations = 0
    successful_combinations = 0
    
    # Generate all possible combinations of tiles without replacement
    tile_combinations = combinations(tiles, n)
    
    # Count the total number of combinations
    for combination in tile_combinations:
        total_combinations += 1
        # Check if the sum of the combination equals the target
        if sum(combination) == t:
            successful_combinations += 1
    
    return successful_combinations, total_combinations - successful_combinations

def main():
    for line in sys.stdin:
        g = int(line)
        for i in range(g):
            m = int(input())
            tiles = list(map(int, input().split()))
            n, t = map(int, input().split())
            
            successful_combinations, total_combinations = calculate_odds(m, tiles, n, t)
            
            print(f"Game {i + 1} -- {successful_combinations} : {total_combinations}")

if __name__ == "__main__":
    main()
