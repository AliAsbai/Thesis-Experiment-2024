def find_missing_number(r1, s):
  """
  This function finds the missing number (R2) given R1 and the mean (S).

  Args:
      r1: The first known number (R1).
      s: The mean of R1 and R2.

  Returns:
      The missing number (R2).
  """
  # Formula for R2: mean (S) * 2 - known number (R1)
  r2 = 2 * s - r1
  return r2

# Get input from the user
r1, s = map(int, input().split())

# Find the missing number
missing_number = find_missing_number(r1, s)

# Print the result
print(missing_number)
