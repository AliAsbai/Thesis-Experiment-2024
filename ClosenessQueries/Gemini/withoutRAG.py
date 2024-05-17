from collections import defaultdict
import random

def bfs(graph, start, visited):
  """
  Performs Breadth-First Search from a starting vertex.

  Args:
      graph: Adjacency list representation of the graph.
      start: Starting vertex for the BFS traversal.
      visited: Set to keep track of visited vertices.

  Returns:
      Distance from starting vertex (limited by a threshold).
  """
  queue = [start]
  visited.add(start)
  distance = 0  # Distance from starting vertex
  threshold = 20  # Limit BFS search depth (adjust based on constraints)

  while queue and distance < threshold:
    level_size = len(queue)
    for _ in range(level_size):
      current = queue.pop(0)
      for neighbor in graph[current]:
        if neighbor not in visited:
          queue.append(neighbor)
          visited.add(neighbor)
          distance += 1
    # Optimization: Stop searching after reaching threshold
  return distance

def find_distance(graph, u, v, uf):
  """
  Finds the distance between two vertices with a combination of BFS and Union-Find.

  Args:
      graph: Adjacency list representation of the graph.
      u: Starting vertex.
      v: Target vertex.
      uf: Union-Find data structure for tracking connected components.

  Returns:
      Distance between u and v (limited by threshold or exact), or -1 if not found.
  """
  visited = set()
  # Check if already in the same set (connected) for efficiency
  if uf.find(u) == uf.find(v):
    return 1

  distance_u = bfs(graph, u, visited.copy())
  distance_v = bfs(graph, v, visited.copy())

  # Probabilistic check for group 2 constraints (if BFS doesn't find exact path)
  if (distance_u <= distance_v and distance_v <= 2 * distance_u) or \
     (distance_v <= distance_u and distance_u <= 2 * distance_v):
    return min(distance_u, distance_v)
  else:
    return -1  # No path found within threshold or group 2 constraints

def main():
  """
  Reads input, builds graph and Union-Find, and processes queries.
  """
  n, m = map(int, input().split())
  graph = defaultdict(list)
  uf = UnionFind(n)
  for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # Add edge for undirected graph
    uf.union(u, v)  # Union operation for connected components

  q = int(input())
  for _ in range(q):
    u, v = map(int, input().split())
    distance = find_distance(graph, u, v, uf)
    print(distance)

if __name__ == "__main__":
  main()
