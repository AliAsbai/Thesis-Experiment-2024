#! /usr/bin/python3

def is_prime(n):
  """
  Primality test using trial division for small numbers.
  """
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

def count_primes(a, b):
  """
  Counts the number of primes between a (inclusive) and b (inclusive).
  """
  count = 0
  # Directly count primes for small ranges (including 2)
  if b - a <= 10**12:
    # Ensure loop starts from 2 for small ranges
    for num in range(2, b + 1):
      if is_prime(num):
        count += 1
  else:
    for num in range(a if a % 2 == 0 else a + 1, b + 1, 2):
      if is_prime(num):
        count += 1
  return count

# Read input
a, b = map(int, input().split())

# Count primes and print result
prime_count = count_primes(a, b)
print(prime_count)
