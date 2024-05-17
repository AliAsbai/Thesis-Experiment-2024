import sys

def max_arithmetic_progression_length(n, c, arr):
    max_length = 1
    dp = [1] * n  # Initialize a list to store maximum lengths
    
    for i in range(1, n):
        dp[i] = dp[i-1] + 1 if arr[i] - arr[i-1] == arr[i-1] - arr[i-2] else 2
    
    max_length = max(dp)
    
    if max_length > n / c:
        return max_length
    else:
        return -1

if __name__ == "__main__":
    for line in sys.stdin:
        t = int(line.strip())
        for _ in range(t):
            n, c = map(int, sys.stdin.readline().strip().split())
            arr = list(map(int, sys.stdin.readline().strip().split()))
            result = max_arithmetic_progression_length(n, c, arr)
            print(result)
