import sys

def solve():
  """
  This function reads input, calculates the smallest toolbar area, and prints the result.
  """
  # Read the number of icons (N)
  n = int(sys.stdin.readline())

  # Read icon sizes and store them in a sorted list (s)
  s = [int(line) for line in sys.stdin]

  # Initialize empty arrays for partial sums (p and q)
  p = [0] * (n + 1)
  q = [0] * (n + 1)

  # Track toggle variable (t)
  t = True

  # Calculate partial sums based on icon sizes
  for i in range(2 * n):
    if t:
      p[i // 2 + 1] = max(p[i // 2 + 1], s[i])
    else:
      q[i // 2 + 1] = max(q[i // 2 + 1], s[i])
    t = not t

  # Calculate minimum toolbar area for each column (k)
  min_area = float('inf')
  for k in range(1, n + 1):
    min_area = min(min_area, (p[k] + q[n - k + 1]))  # Find sum, not maximum

  # Print the minimum toolbar area
  print(int(min_area**2))  # Square the sum for total area

# Run the solver function
solve()
