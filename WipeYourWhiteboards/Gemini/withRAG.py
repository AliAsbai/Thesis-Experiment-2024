#! /usr/bin/python3

def gcd(a, b):
  """Calculates the greatest common divisor of two integers."""
  while b != 0:
    a, b = b, a % b
  return a

def solve(r, s, q):
  """Finds the smallest positive A and B such that A*R + B*S = Q."""
  # Normalize inputs by dividing by their GCD
  d = gcd(r, s)
  r //= d
  s //= d
  q //= d

  # Use Bezout's coefficients to find a and b
  a, b = 1, 0
  u, v = s, r
  while v != 0:
    q, r = u // v, u % v
    u, v = r, q
    a, b = b - a * q, a

  # Rescale a and b by q
  a *= q
  b *= q

  # Adjust a and b for specific conditions
  period_a = s // d  # Calculate period for a
  period_b = r // d  # Calculate period for b
  a = (a % period_a + period_a) % period_a  # Ensure a within period
  b = (b % period_b + period_b) % period_b  # Ensure b within period

  # Ensure a and b are positive
  return min(a, -a), min(b, -b)

def main():
  """Reads input, solves each test case, and prints results."""
  t = int(input())
  for _ in range(t):
    r, s, q = map(int, input().split())
    a, b = solve(r, s, q)
    print(a, b)

if __name__ == "__main__":
  main()
