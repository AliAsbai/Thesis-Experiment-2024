def count_winning_instances(n, board):
    # Initialize a dictionary to store the frequency of each value on the board
    frequency = {}
    for num in board:
        frequency[num] = frequency.get(num, 0) + 1

    # Initialize counts for left and right directions
    left_counts = {}
    right_counts = {}

    # Initialize the total count of winning instances
    total_count = 0

    # Loop through each board square
    for num in board:
        # Update the counts for the current number in left and right directions
        if num > 0:
            right_counts[num] = right_counts.get(num, 0) + 1
        elif num < 0:
            left_counts[num] = left_counts.get(num, 0) + 1

        # Check if the current number is a winning instance
        if -num in right_counts:
            total_count += right_counts[-num]

        # If the current number is negative, check for winning instances in the left direction
        if num < 0:
            total_count += frequency.get(-num, 0)

    return total_count

# Sample Input 1
n1 = 4
board1 = [1, 2, 3, 4]
print(count_winning_instances(n1, board1))  # Output: 7

# Sample Input 2
n2 = 2
board2 = [1, -1]
print(count_winning_instances(n2, board2))  # Output: 4
