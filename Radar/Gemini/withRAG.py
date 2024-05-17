#! /usr/bin/python3

def gcd(a, b):
  """
  This function calculates the greatest common divisor (GCD) of two integers.
  """
  while b != 0:
    a, b = b, a % b
  return a

def chinese_remainder(a, m):
  """
  This function implements the Chinese Remainder Theorem to find a value
  that satisfies the system of congruences x = a_i (mod m_i) for all i.
  """
  M = 1
  for mi in m:
    M *= mi
  all_M = [M // mi for mi in m]
  z = 0
  for i in range(len(a)):
    mi = m[i]
    yi = all_M[i]
    # Handle potential zero denominator by checking GCD first
    if gcd(yi, mi - 1) != 1:
      return None  # No solution exists
    inv_mi = pow(yi, -1, (mi - 1))  # Modular multiplicative inverse
    z = (z + a[i] * inv_mi * all_M[i]) % M
  return z

def solve(m, x, y):
  """
  This function solves the problem for a given set of wavelengths, measurements,
  and accuracies. It finds the smallest possible distance to the lighthouse.
  """
  remainders = [(xi + yi) % mi for xi, yi, mi in zip(x, y, m)]
  solution = chinese_remainder(remainders, m)
  return solution

def main():
  """
  This function reads the input, converts it to integers, and calls the solve
  function for each set of data. It then prints the smallest possible distance
  or "No solution" if none exists.
  """
  for _ in range(int(input())):
    m = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    y = [int(x) for x in input().split()]
    z = solve(m, x, y)
    if z is None:
      print("No solution")
    else:
      print(z)

if __name__ == "__main__":
  main()
