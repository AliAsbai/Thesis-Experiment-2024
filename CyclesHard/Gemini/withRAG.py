#! /usr/bin/python3

MOD = 9901

def dfs(graph, forbidden, visited, current, path, count):
  """
  Performs DFS on the graph to find Hamiltonian cycles.

  Args:
    graph: Adjacency list representation of the graph.
    forbidden: Set of forbidden edges.
    visited: Set of visited nodes.
    current: Current node in the path.
    path: Current path traversed.
    count: Count of Hamiltonian cycles found.

  Returns:
    Count of Hamiltonian cycles found (modulo MOD).
  """
  if len(path) == len(graph):
    # Check if cycle and avoid forbidden edges
    if all(edge not in forbidden for edge in zip(path, path[1:])):
      count = (count + 1) % MOD
    return count

  for neighbor in graph[current]:
    if neighbor not in visited:
      visited.add(neighbor)
      count = dfs(graph, forbidden, visited, neighbor, path + [neighbor], count)
      visited.remove(neighbor)
  return count

def solve(n, k, edges):
  """
  Solves the problem for a single test case.

  Args:
    n: Number of nodes in the graph.
    k: Number of forbidden edges.
    edges: List of forbidden edges.

  Returns:
    Number of Hamiltonian cycles (modulo MOD).
  """
  graph = [[] for _ in range(n + 1)]
  forbidden = set(edges)
  for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

  # Start DFS from each node
  count = 0
  for i in range(1, n + 1):
    count = dfs(graph, forbidden, set([i]), i, [i], count)
  return count

for _ in range(int(input())):
  n, k = map(int, input().split())
  edges = [tuple(map(int, input().split())) for _ in range(k)]
  result = solve(n, k, edges)
  print(f"Case #{_+1}: {result}")
