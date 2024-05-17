import sys

def gcd(a, b):
  """Calculates the greatest common divisor of two integers."""
  while b:
    a, b = b, a % b
  return a

def solve_equations(eq1, eq2):
  """
  Solves a system of two linear equations with two variables.

  Args:
      eq1: The first equation as a string.
      eq2: The second equation as a string.

  Returns:
      A tuple containing two strings: the solution for x and the solution for y.
  """
  # Parse equations
  coeff_x1, coeff_y1, const1 = parse_equation(eq1)
  coeff_x2, coeff_y2, const2 = parse_equation(eq2)

  # Check for dependent or inconsistent equations
  determinant = coeff_x1 * coeff_y2 - coeff_x2 * coeff_y1
  if determinant == 0:
    if coeff_x1 * const2 == coeff_x2 * const1:
      return "inf", "inf"  # Infinite solutions
    else:
      return "no solution", "no solution"  # No solution

  # Solve for x and y
  x = (coeff_y2 * const1 - coeff_y1 * const2) // determinant
  y = (coeff_x1 * const2 - coeff_x2 * const1) // determinant

  # Simplify solution (find gcd)
  common_factor = gcd(abs(x), abs(y))
  x = str(-x // common_factor if x < 0 else x // common_factor)
  y = str(-y // common_factor if y < 0 else y // common_factor)

  return x, y

def parse_equation(equation):
  """
  Parses an equation string into coefficients and constant term.

  Args:
      equation: The equation string.

  Returns:
      A tuple containing three integers: coefficients of x and y, and constant term.
  """
  coeff_x = 0
  coeff_y = 0
  sign = 1  # Reset sign for each equation
  constant_seen = False  # Flag to track constant term

  for term in equation.split():
    if term == "x":
      coeff_x += sign
    elif term == "y":
      coeff_y += sign
    elif term.isdigit():
      if not constant_seen:
        const = int(term) * sign
        constant_seen = True
      else:
        # Handle multiple constants on LHS (shouldn't happen in valid input)
        raise ValueError("Invalid equation format (multiple constants on LHS)")
    else:
      sign = -1 if term == "-" else 1
  return coeff_x, coeff_y, const

# Read input
for line in sys.stdin:
  if line.strip() == "":
    print()
    continue
  num_cases = int(line)
  for _ in range(num_cases):
    eq1 = sys.stdin.readline().strip()
    eq2 = sys.stdin.readline().strip()
    x, y = solve_equations(eq1, eq2)
    print(x)
    print(y)
  print()
