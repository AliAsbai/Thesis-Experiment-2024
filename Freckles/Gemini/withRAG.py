#! /usr/bin/python3

from collections import defaultdict
from math import sqrt


def distance(p1, p2):
  """Calculates the Euclidean distance between two points."""
  return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def find_parent(parent, i):
  """Finds the root of the tree for a given node in the disjoint set."""
  if parent[i] != i:
    parent[i] = find_parent(parent, parent[i])
  return parent[i]


def union(parent, rank, x, y):
  """Unions two sets in the disjoint set forest."""
  xroot = find_parent(parent, x)
  yroot = find_parent(parent, y)

  # Attach smaller rank tree under root of higher rank tree
  if rank[xroot] < rank[yroot]:
    parent[xroot] = yroot
  elif rank[xroot] > rank[yroot]:
    parent[yroot] = xroot
  else:
    parent[yroot] = xroot
    rank[xroot] += 1


def minimum_spanning_tree(points):
  """
  Calculates the minimum spanning tree using Kruskal's algorithm.
  """
  n = len(points)
  parent = [i for i in range(n)]
  rank = [0] * n

  # Create edges with weights (distances) as a list of tuples
  edges = []
  for i in range(n):
    for j in range(i + 1, n):  # Avoid duplicate edges (i, j) and (j, i)
      weight = distance(points[i], points[j])
      edges.append((weight, i, j))  # Edge as (weight, point1, point2)

  # Sort edges by weight (distance)
  edges.sort()

  # Initialize total distance
  total_distance = 0.0

  # Process edges in sorted order
  for weight, p1, p2 in edges:
    # Check if adding the edge creates a cycle
    if find_parent(parent, p1) != find_parent(parent, p2):
      total_distance += weight
      union(parent, rank, p1, p2)

  return total_distance


def main():
  """
  Reads input, calculates minimum spanning tree, and prints the result.
  """
  for _ in range(int(input())):
    n = int(input())
    points = []
    for _ in range(n):
      x, y = map(float, input().split())
      points.append((x, y))

    # Calculate minimum spanning tree
    total_distance = minimum_spanning_tree(points)

    # Print result with two decimal places
    print(f"{total_distance:.2f}")


if __name__ == "__main__":
  main()
