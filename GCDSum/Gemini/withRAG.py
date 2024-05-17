#! /usr/bin/python3

def gcd(a, b):
  """Calculates the greatest common divisor of two numbers."""
  while b:
    a, b = b, a % b
  return a

def phi(n):
  """Calculates Euler's Totient function of a number."""
  if n == 1:
    return 0
  result = n
  p = 2
  while p * p <= n:
    if n % p == 0:
      result -= result // p
      while n % p == 0:
        p += 1
  if n > 1:
    result -= result // n
  return result

def solve(n):
  """Calculates the sum based on the problem description."""
  total = 0
  for d in range(1, n + 1):
    if n % d == 0:
      total += d * phi(n // d)
      # Print n and d for debugging (optional)
      # print(f"d: {d}, n//d: {n//d}, phi(n//d): {phi(n//d)}")
  return total

# Read input
n = int(input())

# Print n for debugging (optional)
# print(f"Input: {n}")

# Calculate and print the sum
print(solve(n))
