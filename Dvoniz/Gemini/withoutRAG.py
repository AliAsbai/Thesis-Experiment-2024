def longest_interesting_subsequences(A, S):
    N = len(A)
    results = [0] * N

    # Precompute prefix sums for efficient sum calculations
    prefix_sums = [0] * (N + 1)
    for i in range(N):
        prefix_sums[i + 1] = prefix_sums[i] + A[i]

    for i in range(N):
        max_k = min(N - i, 2 * (S // A[i]))  # Limit K based on array size and potential overflow

        # Check for interesting subsequences with lengths 2, 4, 6, ...
        for K in range(2, max_k + 1, 2):
            j = i + K - 1
            if j >= N:
                break

            # Optimized sum checks using prefix sums
            if prefix_sums[j + 1] - prefix_sums[i + K // 2] <= S and \
               prefix_sums[i + K // 2] - prefix_sums[i] <= S:
                results[i] = K
            else:
                # Early break optimization
                break

    return results

# Get input
N, S = map(int, input().split())
A = [int(input()) for _in range(N)]

# Solve and print results
results = longest_interesting_subsequences(A, S)
for result in results:
    print(result)
