import heapq

def cheapest_transfer_fee(banks, partnerships, source, target, swerc_banks, tax):
  """
  Calculates the largest fee such that SWERC offers the cheapest transfer between X and Y.

  Args:
      banks: Total number of banks (2 <= banks <= 1000).
      partnerships: Number of transfer partnerships (1 <= partnerships <= 10000).
      source: Source bank identifier (1 <= source <= banks, source != target).
      target: Target bank identifier (1 <= target <= banks, source != target).
      swerc_banks: List of SWERC bank identifiers (length M, 2 <= M <= banks).
      tax: Extra tax on each transfer (integer).

  Returns:
      The largest fee for SWERC to be cheapest, "Infinity" if fee can be infinitely large,
      or "Impossible" if there's no such fee, or "Error" if invalid input is encountered.
  """

  # Create a graph to represent transfer agreements
  graph = {i: [] for i in range(1, banks + 1)}
  for _ in range(partnerships):
    try:
      a, b, c = map(int, input().split())
      if 1 <= a <= banks and 1 <= b <= banks and a != b and 1 <= c <= 1000000000:
        graph[a].append((b, c))
        graph[b].append((a, c))  # Ensure bidirectional connections
      else:
        return "Error: Invalid partnership data"
    except ValueError:
      return "Error: Invalid partnership data (non-integer input)"

  # Function to find the cheapest path using Dijkstra's algorithm
  def dijkstra(start, end):
    distances = {i: float('inf') for i in range(1, banks + 1)}
    distances[start] = 0
    visited = set()
    pq = [(0, start)]

    while pq:
      dist, curr = heapq.heappop(pq)
      if curr in visited:
        continue
      visited.add(curr)

      if curr == end:
        return dist

      for neighbor, cost in graph[curr]:
        new_dist = dist + cost + tax
        if new_dist < distances[neighbor]:
          distances[neighbor] = new_dist
          heapq.heappush(pq, (new_dist, neighbor))

    return float('inf')  # Return infinity if no path is found

  # Handle cases where source or target are not in SWERC banks
  if source not in swerc_banks or target not in swerc_banks:
    # If either source or target is not in SWERC, SWERC cannot be cheapest
    return "Impossible"

  # Find cheapest path within SWERC banks (consider only SWERC banks as neighbors)
  def cheapest_swerc_path(start, end):
    distances = {i: float('inf') for i in range(1, banks + 1)}
    distances[start] = 0
    visited = set()
    pq = [(0, start)]

    while pq:
      dist, curr = heapq.heappop(pq)
      if curr in visited:
        continue
      visited.add(curr)

      if curr == end:
        return dist

      for neighbor, cost in graph[curr]:
        if neighbor in swerc_banks:  # Only consider SWERC banks as neighbors
          new_dist = dist + cost + tax
          if new_dist < distances[neighbor]:
            distances[neighbor] = new_dist
            heapq.heappush(pq, (new_dist, neighbor))

    return float('inf')

  # Find cheapest path within or outside SWERC banks
  cheapest_any_fee = dijkstra(source, target)
  cheapest_swerc_fee = cheapest_swerc_path(source, target)

  # Find the largest fee such that SWERC is cheapest
  largest_fee = max(0, cheapest_any_fee - cheapest_swerc_fee - 1)

  # If fee can be infinitely large, return "Infinity"
  if largest_fee == float('inf'):
    return "Infinity"

  return largest_fee

# Read
