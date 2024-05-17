import numpy as np


def solve_system(A, b):
  """
  Solves the system of equations Ax = b using linear algebra.

  Args:
      A: A numpy array representing the coefficient matrix.
      b: A numpy array representing the constant vector.

  Returns:
      A numpy array representing the solution vector x,
      or "inconsistent" if the system has no solution,
      or "?" if there are infinitely many solutions.
  """

  # Check for invalid input (square matrix and compatible dimensions)
  if len(A.shape) != 2 or A.shape[0] != A.shape[1] or len(b.shape) != 1 or A.shape[0] != b.shape[0]:
    raise ValueError("Invalid input: Matrices must be square and have compatible dimensions.")

  try:
    # Attempt LU decomposition for efficiency (fallback to lstsq if singular)
    x = np.linalg.solve(A, b)
  except np.linalg.LinAlgError as e:
    if "Singular matrix" in str(e):
      # Use lstsq for potentially singular or under-determined systems
      x, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)
      if rank < A.shape[0]:
        return "?"
      elif np.any(singular_values < 1e-10):
        return "inconsistent"
      else:
        return x
    else:
      raise e  # Re-raise other LinAlgErrors

  return x


def main():
  """
  Reads input, solves each test case, and prints the solution.
  """
  while True:
    n = int(input())
    if n == 0:
      break

    try:
      # Read matrix A
      A = np.zeros((n, n))
      for i in range(n):
        A[i] = np.array([float(x) for x in input().split()])

      # Read vector b
      b = np.array([float(x) for x in input().split()])

      # Solve the system
      x = solve_system(A, b)

      # Print the solution
      if isinstance(x, str):
        print(x)
      else:
        print(*x)  # Print each element of x on a separate line
    except ValueError as e:
      print(f"Invalid input: {e}")

if __name__ == "__main__":
  main()
