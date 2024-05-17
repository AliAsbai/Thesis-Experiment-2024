import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst_edges = []
    for edge in edges:
        u, v, weight = edge
        if uf.union(u, v):
            mst_edges.append(edge)
            if len(mst_edges) == n - 1:
                break
    return mst_edges

def min_margin(n, m, sensors):
    edges = [(s[0], s[1], s[2]) for s in sensors]
    mst_edges = kruskal(n, edges)
    max_margin = 0
    for edge in mst_edges:
        max_margin = max(max_margin, abs(edge[2] - sensors[edge[0]][2]), abs(edge[2] - sensors[edge[1]][2]))
    return max_margin

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        m = int(input().strip())
        sensors = []
        for _ in range(m):
            a, b, w = map(int, input().strip().split())
            sensors.append((a, b, w))
        result = min_margin(n, m, sensors)
        print(result)

if __name__ == "__main__":
    main()
