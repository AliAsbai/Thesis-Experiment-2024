def find_quadrant(x, y):
  """
  This function determines the quadrant of a point given its coordinates.

  Args:
      x: The x-coordinate of the point.
      y: The y-coordinate of the point.

  Returns:
      The quadrant number (1, 2, 3, or 4) of the point.
  """

  if x > 0 and y > 0:
    return 1
  elif x < 0 and y > 0:
    return 2
  elif x < 0 and y < 0:
    return 3
  else:  # x > 0 and y < 0
    return 4

# Get input from the user
x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

# Call the function to find the quadrant
quadrant = find_quadrant(x, y)

# Print the result
print("The point lies in quadrant", quadrant)
