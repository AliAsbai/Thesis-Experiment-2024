import sys

def bellman_ford(graph, start, tax):
  """
  Implementation of Bellman-Ford algorithm to find shortest paths with tax.

  Args:
    graph: A dictionary where keys are nodes and values are dictionaries of neighbors and their edge weights.
    start: The starting node for the Bellman-Ford algorithm.
    tax: The extra tax to be added to each edge weight.

  Returns:
    A dictionary containing the shortest distances from the start node to all other nodes,
    or None if there is a negative cycle.
  """
  n = len(graph)
  distance = {node: float('inf') for node in graph}
  distance[start] = 0

  # Relax edges for n iterations (standard Bellman-Ford)
  for _ in range(n):
    for node, neighbors in graph.items():
      for neighbor, weight in neighbors.items():
        distance[neighbor] = min(distance[neighbor], distance[node] + weight + tax)

  # Check for negative cycles in a separate loop
  for node, neighbors in graph.items():
    for neighbor, weight in neighbors.items():
      if distance[neighbor] > distance[node] + weight + tax:
        return None

  return distance

def solve(data):
  """
  Solves the problem of finding the largest fee for SWERC to be the cheapest transfer option.

  Args:
    data: A list containing the input data.

  Returns:
    The largest fee or "Infinity" or "Impossible".
  """
  n, p, x, y = data[0]
  graph = {i: {} for i in range(1, n + 1)}
  for _ in range(p):
    a, b, c = map(int, data[1:])
    graph[a][b] = c
    graph[b][a] = c

  m = int(data[-1][0])
  sw_banks = set(map(int, data[-1][1:]))

  # Find shortest paths without tax for all banks
  distance_without_tax = bellman_ford(graph.copy(), x, 0)

  # Check if there is a path between X and Y
  if distance_without_tax is None or distance_without_tax[y] == float('inf'):
    return "Impossible"

  # Find the largest fee such that SWERC is the cheapest option
  for tax in range(distance_without_tax[y]):
    # Simulate shortest paths for SWERC banks with the current tax
    shortest_path_with_tax = {bank: distance_without_tax[bank] for bank in sw_banks}
    visited = set()  # Keep track of visited nodes within SWERC banks

    for bank in sw_banks:
      if bank in visited:
        continue  # Avoid revisiting nodes within SWERC banks
      visited.add(bank)

      for neighbor, weight in graph[bank].items():
        if neighbor in sw_banks:
          shortest_path_with_tax[neighbor] = min(shortest_path_with_tax[neighbor], shortest_path_with_tax[bank] + weight + tax)

    if shortest_path_with_tax[y] > distance_without_tax[y]:
      return tax

  return "Impossible"

# Read input data
data = []
for line in sys.stdin:
  data.append(list(map(int, line.split())))

# Solve the problem and print the output
result = solve(data)
print(result)
