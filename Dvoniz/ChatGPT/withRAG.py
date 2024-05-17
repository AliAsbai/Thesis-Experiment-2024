import sys

def longest_interesting_subsequence(arr, n, k, s):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    max_length = [0] * n

    # Calculate the length of the longest interesting subsequence for each element
    for i in range(n):
        left, right = max(0, i - k), min(n, i + k + 1)
        left_sum = prefix_sum[i] - prefix_sum[left]
        right_sum = prefix_sum[right] - prefix_sum[i]
        if left_sum <= s:
            max_length[i] = min(n, i + k) - i + 1
        if right_sum <= s:
            max_length[i] = max(max_length[i], i - max(0, i - k) + 1)

    return max_length

def main():
    for line in sys.stdin:
        n, s = map(int, line.split())
        arr = [int(sys.stdin.readline()) for _ in range(n)]

        result = longest_interesting_subsequence(arr, n, n // 2, s)

        for length in result:
            print(length)

if __name__ == "__main__":
    main()
