def is_reachable(start_x, start_y, end_x, end_y, charge):
  """
  This function checks if it's possible to reach the destination
  using exactly the given charge.

  Args:
      start_x: x-coordinate of the starting intersection.
      start_y: y-coordinate of the starting intersection.
      end_x: x-coordinate of the destination intersection.
      end_y: y-coordinate of the destination intersection.
      charge: Initial units of electrical charge in the battery.

  Returns:
      'Y' if reachable with exact charge, 'N' otherwise.
  """
  # Calculate the Manhattan distance (sum of absolute differences)
  distance = abs(start_x - end_x) + abs(start_y - end_y)

  # Check if distance is reachable with the given charge
  if distance <= charge and distance % 2 == charge % 2:
    return 'Y'
  else:
    return 'N'

# Read input
start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())
charge = int(input())

# Call the function and print the output
output = is_reachable(start_x, start_y, end_x, end_y, charge)
print(output)
