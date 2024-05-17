MOD = 10**9 + 7

def solve(seq):
  """
  Calculates the sum of inversions for all possible sequences derived from the input string.

  Args:
      seq: The input string containing characters '0', '1', and '?'.

  Returns:
      The sum of inversions modulo 10^9 + 7.
  """
  O, B, I = 0, 1, 0
  for char in seq:
    if char == "1":
      O = (O + B) % MOD
    elif char == "0":
      I = (I + O) % MOD
    else:
      I = (2*I + O) % MOD
      O = (2*O + B) % MOD
      B = (2*B) % MOD
  return I

# Read input from standard input
data = input().strip()

# Solve the problem and print the result
print(solve(data))
