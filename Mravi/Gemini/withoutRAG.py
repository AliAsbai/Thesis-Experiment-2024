from collections import defaultdict
import math

def solve(n, edges, needs, super_pipes):
  """
  Calculates the minimum amount of liquid Bobi needs to buy.

  Args:
      n: Number of nodes in the tree.
      edges: List of tuples (parent, child, flow, is_super) representing edges.
      needs: List of required liquid amounts for each node (-1 for non-leaf).
      super_pipes: Set of indices of super pipes.

  Returns:
      The minimum amount of liquid required.
  """

  # Build the tree structure
  tree = defaultdict(list)
  for parent, child, _, _ in edges:
    tree[parent].append(child)

  # Perform a DFS to calculate liquid flow at each node
  def dfs(node, parent_flow, visited=set()):
    if needs[node] != -1:  # Leaf node
      return needs[node]

    if node in visited:  # Cycle detection (avoid infinite loops)
      return 0  # No flow for nodes in a cycle

    visited.add(node)  # Mark node as visited

    flow = parent_flow
    remaining_flow = 0  # Track remaining flow for non-super pipes
    for child in tree[node]:
      child_flow = dfs(child, flow if not super_pipes.get(edges.index((node, child, *, *))), visited.copy())
      # Consider non-super pipes only for flow calculation
      if not super_pipes.get(edges.index((node, child, *, *))):
        child_flow_for_parent = child_flow * (edges[edges.index((node, child, *, *))][2] / 100)
        remaining_flow = max(remaining_flow, child_flow_for_parent)

    # Ensure strict flow conservation and handle potential numerical errors
    required_flow = flow + remaining_flow
    epsilon = 1e-6  # Tolerance for numerical errors
    if abs(required_flow) < epsilon:
      required_flow = 0
    return required_flow

  # Start DFS from the root with cycle detection
  required_liquid = dfs(1, 0)
  return required_liquid

# Read input
n = int(input())
edges = []
super_pipes = set()
for _ in range(n - 1):
  parent, child, flow, is_super = map(int, input().split())
  edges.append((parent, child, flow, is_super))
  if is_super:
    super_pipes.add(len(edges) - 1)
needs = list(map(float, input().split()))

# Solve and print result
result = solve(n, edges, needs, super_pipes)
print(f"{result:.4f}")
