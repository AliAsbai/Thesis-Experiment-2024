def longest_interesting_subsequence(N, S, A):
    max_len = 0
    curr_sum = 0
    start = 0

    for i in range(N):
        curr_sum += A[i]

        while curr_sum - A[start] > S:
            curr_sum -= A[start]
            start += 1

        if curr_sum <= S and i - start + 1 > max_len:
            max_len = i - start + 1

    return max_len


# Read input
N, S = map(int, input().split())
A = [int(input()) for _ in range(N)]

# Output the length of the longest interesting subsequence starting with each element
for i in range(N):
    print(longest_interesting_subsequence(N, S, A[i:]))

