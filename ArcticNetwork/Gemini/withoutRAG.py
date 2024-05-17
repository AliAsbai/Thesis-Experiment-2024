from math import sqrt

def distance(outpost1, outpost2):
  """Calculates the Euclidean distance between two outposts."""
  x1, y1 = outpost1
  x2, y2 = outpost2
  return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_min_d(outposts, satellite_channels):
  """Finds the minimum D required for all outposts to connect."""

  # Create a dictionary to store connections via satellite for efficiency
  satellite_connections = {outpost: set() for outpost in outposts}
  for channel in satellite_channels:
    satellite_connections[channel[0]].add(channel[1])
    satellite_connections[channel[1]].add(channel[0])

  # Flag to track if all outposts are connected
  all_connected = False
  current_d = 0  # Initialize D with 0

  while not all_connected:
    all_connected = True
    visited = set()  # Track visited outposts to avoid redundant checks

    # Check for unconnected pairs
    for i in range(len(outposts)):
      outpost1 = outposts[i]
      visited.add(outpost1)  # Mark current outpost as visited

      # Explore connections directly, indirectly (via satellite),
      # and through previously visited outposts for potential paths
      for outpost2 in satellite_connections[outpost1] | visited:
        if outpost2 == outpost1:  # Avoid self-comparison
          continue
        if distance(outpost1, outpost2) <= current_d:
          continue  # Already directly connected

        # Check for indirect connection via outpost2's satellite connections
        indirect_path = any(outpost3 in satellite_connections[outpost2] for outpost3 in visited)
        if indirect_path:
          continue  # Indirect path found

        all_connected = False
        break  # Unconnected pair found, break loop

    # Increase D if not all connected
    if not all_connected:
      current_d += 1

  return current_d

def main():
  """Reads input and calls function to find minimum D."""
  num_cases = int(input())
  for _ in range(num_cases):
    satellite_channels, num_outposts = map(int, input().split())
    outposts = []
    for _ in range(num_outposts):
      outposts.append(tuple(map(int, input().split())))
    min_d = find_min_d(outposts, satellite_channels)
    print(f"{min_d:.2f}")

if __name__ == "__main__":
  main()
