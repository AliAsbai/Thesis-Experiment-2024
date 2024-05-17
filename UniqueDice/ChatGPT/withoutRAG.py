def largest_identical_dice(n, dice_list):
    # Create a dictionary to store counts of each unique combination
    counts = {}
    
    # Iterate through each dice
    for dice in dice_list:
        # Sort the dice to handle rotations
        sorted_dice = tuple(sorted(dice))
        # Increment the count for this combination
        counts[sorted_dice] = counts.get(sorted_dice, 0) + 1
    
    # Find the maximum count
    max_count = max(counts.values())
    
    return max_count

# Input
n = int(input())
dice_list = [list(map(int, input().split())) for _ in range(n)]

# Output
print(largest_identical_dice(n, dice_list))
