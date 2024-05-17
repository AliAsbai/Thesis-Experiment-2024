MOD = 9901

def solve(n, k, forbidden):
  """
  Solves the problem for a given graph with forbidden edges (optimized).

  Args:
      n: Number of nodes in the graph.
      k: Number of forbidden edges.
      forbidden: List of forbidden edges.

  Returns:
      The number of Hamiltonian cycles excluding forbidden edges (mod MOD).
  """
  graph = [[] for _ in range(n)]
  for i in range(n):
    for j in range(i + 1, n):
      graph[i].append(j)
      graph[j].append(i)

  # Initialize sets to track visited nodes and forbidden edges
  visited = set()
  forbidden_set = set(forbidden)

  # Use a stack for iterative exploration
  stack = [(0, 1 << 0)]  # Start with node 0 and itself visited (mask = 1)

  while stack:
    curr_node, mask = stack.pop()

    # Check if all nodes are visited and cycle completes at starting node
    if mask == (1 << n) - 1 and curr_node == 0:
      return 1

    # Explore neighbors
    for neighbor in graph[curr_node]:
      # Check if neighbor is not visited and edge is not forbidden
      if neighbor not in visited and (curr_node, neighbor) not in forbidden_set:
        visited.add(neighbor)
        stack.append((neighbor, mask | (1 << neighbor)))
        visited.remove(neighbor)

  return 0  # No valid cycle found

def main():
  """
  Reads input and calls solve function for each test case.
  """
  t = int(input())
  for case in range(1, t + 1):
    n, k = map(int, input().split())
    forbidden = []
    for _ in range(k):
      u, v = map(int, input().split())
      forbidden.append((u - 1, v - 1))  # Adjust for 0-based indexing
    result = solve(n, k, forbidden)
    print(f"Case #{case}: {result}")

if __name__ == "__main__":
  main()
