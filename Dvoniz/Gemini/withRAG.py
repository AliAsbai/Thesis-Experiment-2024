import sys

def find_max_interesting_length(A, n, s):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    result = [0] * n
    for i in range(n):
        # Find the longest interesting subsequence starting from the left
        left = i
        right = n + 1
        while left < right:
            mid = (left + right) // 2
            if prefix_sum[mid] - prefix_sum[i] <= s:
                left = mid + 1
            else:
                right = mid

        left_max = left - i - 1

        # Fix for right window calculation
        left = 0
        right = i + 1
        while left < right:
            mid = (left + right) // 2
            if prefix_sum[n] - prefix_sum[mid] < s:  # Check against total sum (prefix_sum[n])
                right = mid
            else:
                left = mid + 1

        right_max = i - left + 1  # Update right_max based on new left

        # Combine the results from both sides, considering sum equal to s as interesting
        result[i] = min(left_max, right_max) * 2

    return result

if __name__ == "__main__":
    n, s = map(int, sys.stdin.readline().split())
    A = [int(sys.stdin.readline()) for _ in range(n)]
    result = find_max_interesting_length(A, n, s)
    for length in result:
        print(length)
