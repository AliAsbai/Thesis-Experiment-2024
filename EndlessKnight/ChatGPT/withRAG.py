import sys

# Function to check if a square contains a rock
def is_rock(square, rocks):
    return square in rocks

# Function to count the number of ways to reach each square
def count_ways(H, W, rocks):
    # Initialize an array to store the number of ways to reach each square in the previous row
    prev_row = [0] * (W + 1)
    prev_row[1] = 1

    # Iterate over each row
    for r in range(1, H + 1):
        # Initialize an array to store the number of ways to reach each square in the current row
        curr_row = [0] * (W + 1)
        # Iterate over each square in the current row
        for c in range(1, W + 1):
            # If the square is not a rock, update the number of ways to reach it
            if not is_rock((r, c), rocks):
                # Update the number of ways to reach the current square by summing the number of ways
                # to reach the squares that can jump to it
                for dr, dc in [(2, 1), (1, 2)]:
                    nr, nc = r - dr, c - dc
                    if 1 <= nr <= H and 1 <= nc <= W:
                        curr_row[c] += prev_row[nc]
                        curr_row[c] %= 10007
        # Update the previous row with the current row
        prev_row = curr_row

    # Return the number of ways to reach the bottom-right corner
    return prev_row[W]

# Read input from stdin
for i, line in enumerate(sys.stdin, start=1):
    if i == 1:
        N = int(line)
    else:
        H, W, R = map(int, line.split())
        rocks = set()
        for _ in range(R):
            r, c = map(int, input().split())  # Fixed indexing here
            rocks.add((r, c))
        result = count_ways(H, W, rocks)
        print(f"Case #{i - 1}: {result}")
