#! /usr/bin/python3

MOD = 10**9 + 7

def gcd(a, b):
  """
  Calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
  """
  while b:
    a, b = b, a % b
  return a

def prime_factorize(n):
  """
  Prime factorizes a number n and returns a dictionary containing prime factors and their counts.
  """
  factors = {}
  while n % 2 == 0:
    n //= 2
    factors[2] = factors.get(2, 0) + 1
  i = 3
  while i * i <= n:
    if n % i == 0:
      n //= i
      factors[i] = factors.get(i, 0) + 1
    i += 2
  if n > 1:
    factors[n] = 1
  return factors

def count_divisors(factors):
  """
  Calculates the number of divisors based on the prime factors and their counts.
  """
  count = 1
  for exponent in factors.values():
    count *= (exponent + 1) % MOD
  return count

def main():
  """
  Reads input, calculates the greatest common divisor of all numbers (excluding 1), performs prime factorization of the product divided by the GCD, and calculates the number of divisors.
  """
  n = int(input())
  numbers = list(map(int, input().split()))

  # Calculate GCD excluding 1 to avoid unnecessary divisibility by 1
  gcd_value = 1
  for num in numbers:
    if num != 1:
      gcd_value = gcd(gcd_value, num)

  # Prime factorize the product divided by GCD to avoid redundant factors
  product = 1
  for num in numbers:
    product = (product * num // gcd_value) % MOD
  factors = prime_factorize(product)
  divisors = count_divisors(factors)
  print(divisors)

if __name__ == "__main__":
  main()
