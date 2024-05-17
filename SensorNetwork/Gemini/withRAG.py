#! /usr/bin/python3

def find_min_margin(graph, voltages):
  """
  Finds the minimum margin for an admissible subset of sensors.

  Args:
      graph: A dictionary representing the sensor network graph. 
              Keys are sensor IDs, values are lists of neighboring sensor IDs.
      voltages: A list containing the recommended voltage for each sensor.

  Returns:
      The minimum margin for an admissible subset of sensors.
  """
  n = len(graph)  # Number of sensors

  # Function to check if a subset of sensors covers all doors
  def is_admissible(subset):
    covered_doors = set()
    for sensor in subset:
      covered_doors.update(graph[sensor])
    return len(covered_doors) == n

  # Recursive function to find the minimum margin for a subset
  def dfs(subset, current_margin, visited):
    if is_admissible(subset):
      return current_margin

    min_margin = float('inf')
    for neighbor in graph[subset[0]]:  # Explore neighbors of the first sensor
      if neighbor not in subset and neighbor not in visited:
        visited.add(neighbor)
        new_margin = max(current_margin, abs(voltages[neighbor] - voltages[subset[0]]))
        min_margin = min(min_margin, dfs(subset | {neighbor}, new_margin, visited.copy()))
        visited.remove(neighbor)
    return min_margin

  return dfs(set([0]), 0, set())  # Start exploration from sensor 0 with visited set

for line in sys.stdin:
  # Read input data
  n = int(line)
  if n == 0:
    break

  m = int(sys.stdin.readline())
  graph = {}
  voltages = []
  for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().split())
    graph.setdefault(a, []).append(b)
    graph.setdefault(b, []).append(a)
    voltages.append(w)

  # Find minimum margin
  min_margin = find_min_margin(graph, voltages)

  # Print output
  print(min_margin)
