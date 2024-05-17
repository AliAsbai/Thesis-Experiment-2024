def max_arithmetic_subsequence_length(n, c, arr):
    max_length = 0
    dp = [1] * n  # Initialize all elements with 1 as the minimum length

    for i in range(1, n):
        for j in range(i):
            diff = arr[i] - arr[j]
            if diff % c == 0:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])

    return max_length if max_length > n / c else -1

# Reading input
t = int(input().strip())
for _ in range(t):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    result = max_arithmetic_subsequence_length(n, c, arr)
    print(result)
