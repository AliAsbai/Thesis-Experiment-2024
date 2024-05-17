from math import gcd

def smallest_distance(m1, m2, m3, x1, x2, x3, y1, y2, y3):
  """
  Finds the smallest possible distance to the lighthouse.

  Args:
      m1, m2, m3: Wavelengths (positive prime numbers).
      x1, x2, x3: Measurements (nonnegative integers).
      y1, y2, y3: Accuracies (nonnegative integers).

  Returns:
      The smallest possible distance (nonnegative integer).
  """
  # Calculate residues considering accuracy for each wavelength
  z1 = (x1 - y1) % m1
  z2 = (x2 - y2) % m2
  z3 = (x3 - y3) % m3

  # GCD of differences between residues and their respective wavelengths
  gcd_diff = gcd(m1 - z1, gcd(m2 - z2, m3 - z3))

  # No solution if GCD is not a divisor of all wavelengths
  if gcd_diff not in [m1, m2, m3]:
    return -1

  # Find the smallest multiple of all wavelengths divisible by gcd_diff
  lcm = (m1 * m2 * m3) // gcd_diff

  # Chinese Remainder Theorem (CRT) to find a solution within the LCM range
  solution = crt([z1, z2, z3], [m1, m2, m3], lcm)

  # Check if the solution falls within the valid range for all wavelengths
  if is_valid(solution, z1, y1, m1) and \
     is_valid(solution, z2, y2, m2) and \
     is_valid(solution, z3, y3, m3):
    return solution

  # No solution found using CRT, try exhaustive search within the LCM range
  for i in range(lcm):
    if is_valid(i, z1, y1, m1) and \
       is_valid(i, z2, y2, m2) and \
       is_valid(i, z3, y3, m3):
      return i

  # No solution found after exhaustive search
  return -1

def crt(residues, moduli, m):
  """
  Implements the Chinese Remainder Theorem to find a solution.
  """
  M = prod(moduli)
  solutions = [pow(moduli[i], M - 2, moduli[i]) for i in range(len(residues))]
  return sum(residues[i] * M * solutions[i] % m for i in range(len(residues))) % m

def is_valid(distance, residue, accuracy, m):
  """
  Checks if a distance falls within the valid range for a wavelength.
  """
  return distance % m >= residue - accuracy and distance % m <= residue + accuracy

def prod(iterable):
  """
  Product function for convenience.
  """
  return reduce(lambda x, y: x * y, iterable, 1)

# Read input (same as before)
# ...

# Find the smallest distance
z = smallest_distance(m1, m2, m3, x1, x2, x3, y1, y2, y3)

# Print the answer
print(z)
