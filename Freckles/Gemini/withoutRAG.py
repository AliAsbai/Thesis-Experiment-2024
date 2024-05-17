from math import sqrt
import heapq

class Edge:
  def __init__(self, source, dest, weight):
    self.source = source
    self.dest = dest
    self.weight = weight

def distance(p1, p2):
  """Calculates the Euclidean distance between two points."""
  x1, y1 = p1
  x2, y2 = p2
  return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def create_graph(freckles):
  """Creates a graph with edges between all freckles."""
  n = len(freckles)
  graph = [[] for _ in range(n)]  # Adjacency list representation
  for i in range(n):
    for j in range(n):
      if i != j:  # Avoid self-loops
        weight = distance(freckles[i], freckles[j])
        graph[i].append(Edge(i, j, weight))
  return graph

def minimum_ink(graph):
  """Calculates the minimum total length of ink to connect all freckles using Prim's algorithm."""
  n = len(graph)

  # Use Prim's algorithm with min-heap for efficient edge processing
  mst_cost = 0
  visited = [False] * n
  parent = [-1] * n

  # Start with any random freckle
  visited[0] = True

  # Min-heap for storing edges to explore, sorted by weight
  pq = []
  for edge in graph[0]:  # Add edges from starting freckle
    heapq.heappush(pq, (edge.weight, edge.dest))

  while pq:
    min_weight, min_index = heapq.heappop(pq)
    if not visited[min_index]:
      visited[min_index] = True
      mst_cost += min_weight

      # Add edges from the newly visited freckle
      for edge in graph[min_index]:
        if not visited[edge.dest]:
          heapq.heappush(pq, (edge.weight, edge.dest))

  return mst_cost

def main():
  """Reads input, calculates minimum ink, and prints the result."""
  num_cases = int(input())

  for _ in range(num_cases):
    n = int(input())
    freckles = []
    for _ in range(n):
      x, y = map(float, input().split())
      freckles.append((x, y))

    graph = create_graph(freckles)
    minimum_length = minimum_ink(graph)
    print(f"{minimum_length:.2f}")
    print()  # Blank line between outputs

if __name__ == "__main__":
  main()
