def intersection_count(n):
  """
  Calculates the number of intersections between pairs of diagonals in a convex N-gon
  with no three diagonals intersecting in a single point.

  Args:
      n: The number of vertices in the polygon (3 <= n <= 100).

  Returns:
      The number of intersections between pairs of diagonals.
  """

  # Handle base cases (triangle and square have no intersections)
  if n == 3 or n == 4:
    return 0

  # For n >= 5, each vertex can contribute intersections with n-3 other diagonals
  # We subtract 1 to avoid double counting intersections (each intersection involves two diagonals)
  intersections = n * (n - 3) - 1

  # Additional correction for n=6 (hexagon): three pairs of opposite diagonals intersect twice
  if n == 6:
    intersections -= 3

  return intersections

# Example usage
n = 6
intersections = intersection_count(n)
print(f"Number of intersections for N={n}: {intersections}")
