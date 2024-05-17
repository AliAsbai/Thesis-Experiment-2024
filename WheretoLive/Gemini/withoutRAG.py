def calculate_average_squared_distance(location, points):
  """
  Calculates the average squared distance from a location to all points.

  Args:
      location: A tuple representing the coordinates (x, y) of the location.
      points: A list of tuples representing the coordinates of points of interest.

  Returns:
      The average squared distance from the location to all points.
  """
  total_distance = 0
  for point in points:
    x_diff = location[0] - point[0]
    y_diff = location[1] - point[1]
    total_distance += x_diff**2 + y_diff**2
  return total_distance / len(points)

def find_optimal_location(points):
  """
  Finds the location on the grid with the minimum average squared distance to all points.

  Args:
      points: A list of tuples representing the coordinates of points of interest.

  Returns:
      A tuple representing the coordinates (x, y) of the optimal location.
  """
  min_distance = float('inf')
  best_locations = []  # List to store all locations with min distance
  # Iterate through all possible grid points
  for x in range(1001):
    for y in range(1001):
      distance = calculate_average_squared_distance((x, y), points)
      if distance < min_distance:
        min_distance = distance
        best_locations = [(x, y)]  # Reset best locations list
      elif distance == min_distance:
        best_locations.append((x, y))  # Add location if distance ties
  # Break tie by choosing location with smallest x and then y
  return min(best_locations, key=lambda loc: (loc[0], loc[1]))

def main():
  while True:
    n = int(input())
    if n == 0:
      break
    points = []
    for _ in range(n):
      x, y = map(int, input().split())
      points.append((x, y))
    optimal_location = find_optimal_location(points)
    print(*optimal_location)

if __name__ == "__main__":
  main()
