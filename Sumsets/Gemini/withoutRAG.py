def find_largest_d(S):
  """
  Finds the largest d such that a + b + c = d where a, b, c and d are distinct elements of S.

  Args:
      S: A set of distinct integers.

  Returns:
      The largest d if found, otherwise "no solution".
  """

  # Track potential sums and their complements for negative numbers
  potential_sums = set()
  complement_sums = set()

  for i in S:
    # Check existing sums and their complements for d (avoid duplicates)
    for sum_ in potential_sums:
      if sum_ + i in S and sum_ + i != i:  # Ensure distinct elements
        return sum_ + i  # d found
    for complement in complement_sums:
      if i + complement in S and i + complement != i:  # Ensure distinct elements
        return i + complement  # d found

    # Update potential sums and complements (avoid duplicates, handle negatives)
    potential_sums.update(j + i for j in S if j < i and (j + i) > 0 and j + i not in S)
    complement_sums.update(i - j for j in S if j < i and (i - j) > 0 and i - j not in S)

  # No solution found
  return "no solution"

# Read input
N = int(input())
S = set()
for _ in range(N):
  S.add(int(input()))

# Find and print the largest d
largest_d = find_largest_d(S)
print(largest_d)
