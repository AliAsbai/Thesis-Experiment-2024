def other_endpoint(endpoint):
  """
  Calculates the coordinates of the other endpoint of the dividing line segment.

  Args:
      endpoint: A tuple (x, y) representing the coordinates of one endpoint.

  Returns:
      A tuple (x, y) representing the coordinates of the other endpoint, rounded to two decimal places.
  """
  x, y = endpoint
  # Since the pool is an isosceles right triangle with legs of length 250, the hypotenuse is 250 * sqrt(2)
  from math import sqrt  # Import the math library for square root function
  hypotenuse = 250 * sqrt(2)

  # Check on which edge the endpoint lies
  if x == 0:  # Left edge
    other_x = hypotenuse
    other_y = y
  elif y == 0:  # Bottom edge
    other_x = x
    other_y = hypotenuse
  else:
    raise ValueError("Invalid endpoint. Endpoint must be on the left or bottom edge of the pool.")

  return round(other_x, 2), round(other_y, 2)

# Example usage
endpoint = (0, 50)  # Left edge, y-coordinate can be any value on the edge
other_end = other_endpoint(endpoint)
print(f"The other endpoint is: ({other_end[0]}, {other_end[1]})")
