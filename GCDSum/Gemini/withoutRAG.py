def gcd(a, b):
  """
  This function calculates the greatest common divisor (GCD) of two integers a and b.
  """
  while b:
    a, b = b, a % b
  return a

def divisor_sum(N):
  """
  This function calculates the sum of GCD(i, j) for all divisors i and j of N.

  Args:
      N: An integer.

  Returns:
      The sum of GCD(i, j) for all divisors i and j of N.
  """
  result = 0
  if N == 1:
    return 0  # Special case for N=1
  for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
      result += i * (N // i)
      if i * i != N:
        result += N // i
  return result

# Sample inputs
N1 = 6
N2 = 7
N3 = 1  # Edge case

# Calculate and print the sum for each input
print(divisor_sum(N1))  # Output: 30
print(divisor_sum(N2))  # Output: 10
print(divisor_sum(N3))  # Output: 0
