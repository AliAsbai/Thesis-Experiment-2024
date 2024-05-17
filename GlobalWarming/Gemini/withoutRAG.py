def min_co2(n, m, friends):
  """
  This function finds the minimum total CO2 emission for grouping friends.

  Args:
      n: Number of students in the class.
      m: Number of pairs of friends.
      friends: List of tuples (p, q, c) representing friends and CO2 emission.

  Returns:
      Minimum total CO2 emission or "impossible" if grouping is not possible.
  """

  # Create an adjacency list to represent friendship connections.
  adj_list = [[] for _ in range(n + 1)]
  for p, q, c in friends:
    adj_list[p].append((q, c))
    adj_list[q].append((p, c))

  # Use Union-Find data structure for efficient group management.
  class UnionFind:
    def __init__(self, n):
      self.parent = [i for i in range(n + 1)]
      self.rank = [0] * (n + 1)

    def find(self, x):
      if x != self.parent[x]:
        self.parent[x] = self.find(self.parent[x])
      return self.parent[x]

    def union(self, x, y):
      rx = self.find(x)
      ry = self.find(y)
      if self.rank[rx] < self.rank[ry]:
        self.parent[rx] = ry
      elif self.rank[rx] > self.rank[ry]:
        self.parent[ry] = rx
      else:
        self.parent[ry] = rx
        self.rank[rx] += 1

  # Create and use UnionFind instance for grouping.
  uf = UnionFind(n)
  total_co2 = 0

  # Handle potential edge cases:
  # 1. Odd number of students: Grouping is impossible.
  if n % 2 != 0:
    return "impossible"

  # 2. Friend connections might not form complete groups:
  #   - Check if every student has at least one friend.
  for i in range(1, n + 1):
    if not adj_list[i]:
      return "impossible"

  # Process friends based on CO2 emission (potentially improve efficiency).
  for p, q, c in sorted(friends, key=lambda x: x[2]):
    if uf.find(p) != uf.find(q):
      uf.union(p, q)
      total_co2 += c

  # All students must be connected in a single group.
  if len(set(uf.find(i) for i in range(1, n + 1))) != 1:
    return "impossible"

  return total_co2

# Read input
n, m = map(int, input().split())
friends = []
for _ in range(m):
  p, q, c = map(int, input().split())
  friends.append((p, q, c))

# Find minimum CO2 emission
result = min_co2(n, m, friends)

# Print output
print(result)
