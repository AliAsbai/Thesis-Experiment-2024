import sys

def min_arrows_to_pop(N, heights):
    if N == 0:
        return 0
    
    arrows = 1
    prev_height = heights[0]
    
    for i in range(1, N):
        if heights[i] > prev_height:
            arrows += 1
            prev_height = heights[i]
    
    return arrows

if __name__ == "__main__":
    for line in sys.stdin:
        N = int(line)
        heights = list(map(int, input().split()))
        heights.sort()  # Sort the heights
        print(min_arrows_to_pop(N, heights)))
