#! /usr/bin/python3

class DisjointSet:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [0] * n

  def find(self, u):
    if self.parent[u] != u:
      self.parent[u] = self.find(self.parent[u])
    return self.parent[u]

  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)
    if root_x == root_y:
      return
    if self.rank[root_x] > self.rank[root_y]:
      self.parent[root_y] = root_x
    else:
      self.parent[root_x] = root_y
      if self.rank[root_x] == self.rank[root_y]:
        self.rank[root_y] += 1

def min_cost_pairing(graph):
  n = len(graph)
  min_cost = 0
  visited = [False] * n
  for i in range(n):
    if not visited[i]:
      min_cost_edge = float('inf')  # Initialize with a very high value
      for j in range(n):
        if graph[i][j] != -1 and not visited[j]:
          min_cost_edge = min(min_cost_edge, graph[i][j])
      min_cost += min_cost_edge
      visited[i] = True
      for j in range(n):
        if graph[i][j] != -1:
          visited[j] = True
  return min_cost

def main():
  n, m = map(int, input().split())
  graph = [[-1] * n for _ in range(n)]
  for _ in range(m):
    u, v, cost = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = cost
    graph[v][u] = cost

  disjoint_set = DisjointSet(n)
  for u in range(n):
    for v in range(u + 1, n):
      if graph[u][v] != -1:
        disjoint_set.union(u, v)

  islands = set()
  for i in range(n):
    islands.add(disjoint_set.find(i))

  if len(islands) != 1:
    print("impossible")
    return

  total_cost = 0
  for island in islands:
    island_graph = [[graph[i][j] for j in range(n) if graph[i][j] != -1] for i in range(n) if disjoint_set.find(i) == island]
    total_cost += min_cost_pairing(island_graph)

  print(total_cost)

if __name__ == "__main__":
  main()
