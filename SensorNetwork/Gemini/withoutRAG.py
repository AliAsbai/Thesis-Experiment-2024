def find_min_margin(doors, sensors):
  """
  Finds the minimum margin for an admissible subset of sensors.

  Args:
      doors: Number of doors in the building.
      sensors: List of (door1, door2, recommended_voltage) tuples.

  Returns:
      The minimum margin for an admissible subset of sensors,
      or -1 if no admissible subset exists.
  """
  # Convert doors and sensors to sets for faster membership checks
  door_set = set(range(doors))
  sensor_set = set(tuple(sensor) for sensor in sensors)

  # Function to check if a subset of sensors is admissible
  def is_admissible(subset):
    covered_doors = set()
    for sensor in subset:
      covered_doors.update(sensor[:2])
    return covered_doors == door_set

  # Minimum margin seen so far (initialize with a large value)
  min_margin = float('inf')

  def dfs(current_subset, current_margin):
    """
    Depth-First Search to find admissible subsets with minimum margin.

    Args:
        current_subset: Set of sensors in the current subset.
        current_margin: Current maximum difference in voltages.
    """
    nonlocal min_margin

    # Check if all doors are covered and update minimum margin
    if is_admissible(current_subset):
      min_margin = min(min_margin, current_margin)
      return

    # Explore possibilities by adding neighboring sensors with early termination
    for sensor in sensor_set - current_subset:
      neighbor_doors = sensor[:2]
      # Check for invalid configurations:
      if len(neighbor_doors & current_subset) != 1:  # Sensor controls too few or too many doors
        continue
      if max(current_subset, key=lambda x: x[2])[2] > sensor[2]:  # Voltage constraint violated
        continue

      new_margin = max(current_margin, abs(sensor[2] - max(current_subset, key=lambda x: x[2])[2]))
      # Early termination if new margin exceeds minimum seen so far
      if new_margin >= min_margin:
        return
      dfs(current_subset | {sensor}, new_margin)

  # Start DFS with an empty subset and margin of 0
  dfs(set(), 0)

  # Handle case where no admissible subset exists
  if min_margin == float('inf'):
    return -1

  return min_margin

# Read input
while True:
  # Read number of doors and sensors (handle potential errors)
  try:
    doors = int(input())
    sensors = []
    for _ in range(int(input())):
      sensors.append(tuple(map(int, input().split())))
  except ValueError:
    break

  # Check if end of input
  if doors == 0:
    break

  # Find minimum margin for the current test case
  min_margin = find_min_margin(doors, sensors)

  # Print the minimum margin (or indicate no solution)
  if min_margin == -1:
    print("No solution")
  else:
    print(min_margin)
