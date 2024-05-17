import sys
from math import sqrt


def distance(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def prim(points, satellites):
  # Initialize
  outposts = len(points)
  parent = [-1] * outposts
  key = [float('inf')] * outposts
  key[0] = 0  # Start from the first outpost
  mst_set = [False] * outposts

  # Iterate through all outposts
  for _ in range(outposts):
    min_index = -1
    min_key = float('inf')

    # Find the minimum key outpost from the remaining ones
    for v in range(outposts):
      if mst_set[v] == False and key[v] < min_key:
        min_index = v
        min_key = key[v]

    # Add the picked outpost to MST Set
    mst_set[min_index] = True

    # Update key and parent of the adjacent outposts
    for v in range(outposts):
      # Processing not yet included outposts with a lower distance
      if mst_set[v] == False and distance(points[min_index], points[v]) < key[v]:
        parent[v] = min_index
        key[v] = distance(points[min_index], points[v])

  # Consider only edges less than required satellite connections 
  total_distance = 0  
  for i in range(1, outposts):
      if i < outposts - satellites:
          total_distance += distance(points[parent[i]], points[i])

  return total_distance


def minimum_d(satellites, outposts, points):
  # Find minimum distance using Prim's algorithm
  min_dist = prim(points, satellites)

  return f"{min_dist:.2f}"


# Read input
for line in sys.stdin:
  satellites, outposts = map(int, line.split())
  points = []
  for _ in range(outposts):
    points.append(tuple(map(int, sys.stdin.readline().split())))

  # Calculate minimum distance
  result = minimum_d(satellites, outposts, points)
  print(result)
