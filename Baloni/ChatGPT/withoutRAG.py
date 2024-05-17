def min_arrows_to_pop(N, heights):
    if N == 0:
        return 0
    arrows = 1
    prev_height = heights[0]
    for i in range(1, N):
        if heights[i] != prev_height:
            arrows += 1
            prev_height = heights[i]
    return arrows

# Reading input
N = int(input())
heights = list(map(int, input().split()))

# Sort the heights
heights.sort()

# Calculating and printing the result
result = min_arrows_to_pop(N, heights)
print(result)
