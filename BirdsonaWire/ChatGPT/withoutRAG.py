def max_additional_birds(l, d, n, bird_positions):
    # Sort bird positions
    bird_positions.sort()

    max_additional = 0

    # Calculate space between birds and at the ends
    spaces = []
    spaces.append(bird_positions[0] - 6)
    for i in range(1, n):
        spaces.append(bird_positions[i] - bird_positions[i-1] - 2 * d)
    spaces.append(l - bird_positions[-1] - 6)

    # Calculate additional birds that can fit
    for space in spaces:
        max_additional += max(0, space // (d + 1))

    return max_additional

# Sample input parsing
l, d, n = map(int, input().split())
bird_positions = [int(input()) for _ in range(n)]

# Calculate and print the maximum additional birds
print(max_additional_birds(l, d, n, bird_positions))
