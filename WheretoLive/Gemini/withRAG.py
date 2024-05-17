#! /usr/bin/python3

def calculate_distance(point1, point2):
  """
  Calculates the squared distance between two points.
  """
  x1, y1 = point1
  x2, y2 = point2
  return (x1 - x2) ** 2 + (y1 - y2) ** 2

def find_optimal_location(locations):
  """
  Finds the grid location with the minimum average squared distance
  to all the provided locations.
  """
  min_x = min(location[0] for location in locations)
  min_y = min(location[1] for location in locations)
  current_x, current_y = min_x, min_y
  total_distance = sum(calculate_distance((current_x, current_y), location) for location in locations)

  while True:
    # Check right movement
    right_distance = sum(calculate_distance((current_x + 1, current_y), location) for location in locations)
    # Check up movement
    up_distance = sum(calculate_distance((current_x, current_y + 1), location) for location in locations)

    # Find the direction with the minimum distance change
    min_distance_change = min(right_distance - total_distance, up_distance - total_distance)

    if min_distance_change <= 0:
      break

    # Choose the direction with the minimum distance decrease, 
    # prioritizing ties with smaller x-coordinate
    if right_distance - total_distance < up_distance - total_distance:
      current_x += 1
    elif right_distance - total_distance > up_distance - total_distance:
      current_y += 1
    else:  # Tie in distance change, choose smaller x-coordinate
      current_x += 1

    total_distance = min(right_distance, up_distance)

  return current_x, current_y

for line in sys.stdin:
  num_locations = int(line)
  if num_locations == 0:
    break
  locations = []
  for _ in range(num_locations):
    x, y = map(int, sys.stdin.readline().strip().split())
    locations.append((x, y))
  optimal_x, optimal_y = find_optimal_location(locations)
  print(optimal_x, optimal_y)
