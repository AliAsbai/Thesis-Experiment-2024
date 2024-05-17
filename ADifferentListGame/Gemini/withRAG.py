#! /usr/bin/python3

def prime_factorize(n):
  """
  This function factors a number n into its prime factorization.
  """
  factors = []
  while n % 2 == 0:
    factors.append(2)
    n //= 2
  i = 3
  while i <= n:
    if n % i == 0:
      factors.append(i)
      n //= i
    i += 2
  return factors

def main():
  # Read input
  X = int(input())

  # Prime factorize X
  factors = prime_factorize(X)

  # Count the number of groups (factors with same exponent)
  k = 0
  prev_factor = None
  for factor in factors:
    if factor != prev_factor:
      k += 1
    prev_factor = factor

  # Print the number of points (k)
  print(k)

if __name__ == "__main__":
  main()
