from math import sqrt

def distance(city1, city2):
  """Calculates the Euclidean distance between two cities."""
  x1, y1 = city1
  x2, y2 = city2
  return int(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

def nearest_neighbor(cities):
  """
  Solves TSP using Nearest Neighbor heuristic.

  Args:
      cities: A list of city coordinates (x, y) tuples.

  Returns:
      A list representing the order of visiting cities (0-based index).
  """
  n = len(cities)
  visited = [False] * n
  tour = [0]
  visited[0] = True

  # Build the tour by finding the nearest unvisited city at each step
  for _ in range(1, n):
    min_dist = float('inf')
    min_index = -1
    for i in range(n):
      if not visited[i] and distance(cities[tour[-1]], cities[i]) < min_dist:
        min_dist = distance(cities[tour[-1]], cities[i])
        min_index = i
    tour.append(min_index)
    visited[min_index] = True

  return tour

def main():
  """Reads input, solves TSP, and prints the tour."""
  n = int(input())
  cities = []
  for _ in range(n):
    x, y = map(float, input().split())
    cities.append((x, y))

  tour = nearest_neighbor(cities)
  for city in tour:
    print(city)

if __name__ == "__main__":
  main()
