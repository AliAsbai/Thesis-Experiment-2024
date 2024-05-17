#! /usr/bin/python3

def solve(n, c, a):
  """
  Finds the maximum length arithmetic progression subsequence.

  Args:
      n: Length of the array.
      c: Minimum ratio for the subsequence length.
      a: The array of numbers.

  Returns:
      The maximum length of the subsequence, or -1 if no subsequence satisfies the condition.
  """
  max_len = 0

  # Check all elements as potential starting points
  for i in range(n):
    # Check differences with subsequent elements
    for j in range(i + 1, n):
      diff = a[j] - a[i]
      # Validate difference and avoid zero shift
      if diff and i + diff < n and a[i + diff] == a[i] + diff:
        # Check if subsequence satisfies the condition
        k = i + 2 * diff
        while k < n and a[i] + diff * (k - i) == a[k]:
          k += 1
        subsequence_len = k - i
        if subsequence_len > n // c:
          max_len = max(max_len, subsequence_len)
          break  # Early termination if condition is already met

  return max_len if max_len > 0 else -1

# Read input
for line in sys.stdin:
  n, c = map(int, line.split())
  a = list(map(int, sys.stdin.readline().split()))
  result = solve(n, c, a)
  print(result)
