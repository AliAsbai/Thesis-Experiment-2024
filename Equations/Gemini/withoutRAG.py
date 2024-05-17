import numpy as np
from fractions import Fraction

def parse_equation(equation):
  """Parses an equation string into a coefficient matrix and constant vector."""
  coefficients = [0, 0]
  constant = 0
  sign = 1
  for term in equation.split():
    if term == "x":
      coefficients[0] += sign
    elif term == "y":
      coefficients[1] += sign
    elif term == "=":
      sign = -1
    else:
      constant += sign * int(term)
    sign = 1
  return np.array(coefficients), constant

def solve_system(eq1, eq2):
  """Solves a system of linear equations with two variables using numpy.linalg.solve."""
  A = np.vstack([parse_equation(eq) for eq in [eq1, eq2]])[:, 0]  # Get coefficient matrix
  b = np.array([parse_equation(eq) for eq in [eq1, eq2]])[:, 1]  # Get constant vector
  try:
    x = np.linalg.solve(A, b)  # Solve using numpy.linalg.solve
    return Fraction(x[0]), Fraction(x[1])
  except np.linalg.LinAlgError:
    # Check for dependent or inconsistent system
    if np.allclose(A[0] * np.linalg.inv(A[1]), A[1]):  # Dependent system
      return "many solutions"
    elif np.linalg.cond(A) >= 1e15:  # Handle near-singular matrices (potential numerical issues)
      return "don't know (potentially near-singular system)"
    else:  # Inconsistent system
      return "don't know"

def main():
  """Reads input, solves equations, and prints results."""
  num_tests = int(input())
  for _ in range(num_tests):
    while True:
      eq1 = input()
      if not eq1:
        break
      eq2 = input()
      x, y = solve_system(eq1, eq2)
      if isinstance(x, str):
        print(x)
      else:
        print(x)
        print(y)
      print()

if __name__ == "__main__":
  main()
