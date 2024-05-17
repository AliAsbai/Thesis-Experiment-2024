def gcd(a, b):
  """
  Calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

  Args:
      a: First integer.
      b: Second integer.

  Returns:
      The GCD of a and b.
  """
  while b != 0:
    a, b = b, a % b
  return a

def find_smallest_solution(r, s, q):
  """
  Finds the smallest positive solution (A, B) for A * R + B * S = Q.

  Args:
      r: Integer value from the intermediate result (R >= 2).
      s: Integer value from the intermediate result (S <= -2).
      q: Integer value from the intermediate result (Q >= 1).

  Returns:
      A tuple containing the smallest positive solution (A, B) or None if no solution exists.
  """
  # Handle negative S and calculate GCD
  s_abs = abs(s)
  gcd_val = gcd(r, s_abs)

  # Check if Q is divisible by GCD(R, S)
  if q % gcd_val != 0:
    return None  # No solution exists if Q is not divisible by GCD

  # Solve Bezout's identity using Extended Euclidean Algorithm
  a1, a2 = 1, 0
  b1, b2 = 0, 1
  while s_abs > 0:
    q, r = divmod(r, s_abs)
    a1, a2 = a2, a1 - q * a2
    b1, b2 = b2, b1 - q * b2
    r, s_abs = s_abs, r

  # Calculate A and B considering signs and divisibility by GCD
  a = ((q // gcd_val) + a1) * gcd_val  # Ensure A is always positive
  b = ((-q // gcd_val) + b1) * gcd_val  # Ensure B is always positive

  return a, b  # Solution found

def main():
  # Read number of test cases
  t = int(input())

  for _ in range(t):
    r, s, q = map(int, input().split())
    solution = find_smallest_solution(r, s, q)
    if solution:
      print(*solution)
    else:
      print("No solution")

if __name__ == "__main__":
  main()

