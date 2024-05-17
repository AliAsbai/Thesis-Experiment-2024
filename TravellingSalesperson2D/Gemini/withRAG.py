#! /usr/bin/python3

import sys

def distance(city1, city2):
  """
  Calculates the Euclidean distance between two cities.
  """
  x1, y1 = city1
  x2, y2 = city2
  return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

def nearest_neighbor(cities):
  """
  Implements the Nearest Neighbor algorithm for TSP.
  """
  n = len(cities)
  tour = [0]  # Start at city 0
  visited = set([0])
  for _ in range(1, n):
    best_city = None
    best_dist = float('inf')
    for city in range(n):
      if city not in visited and distance(cities[tour[-1]], cities[city]) < best_dist:
        best_city = city
        best_dist = distance(cities[tour[-1]], cities[city])
    tour.append(best_city)
    visited.add(best_city)
  return tour

def main():
  """
  Reads input, solves TSP using nearest neighbor, and prints output.
  """
  for line in sys.stdin:
    n = int(line)
    cities = []
    for _ in range(n):
      x, y = map(float, sys.stdin.readline().strip().split())
      cities.append((x, y))
    tour = nearest_neighbor(cities)
    for city in tour:
      print(city)

if __name__ == "__main__":
  main()
