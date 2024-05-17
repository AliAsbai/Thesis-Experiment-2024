import sys
import math

class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def kruskal(edges, n, s):
    edges.sort()
    ds = DisjointSet(n)
    count = 0
    for weight, u, v in edges:
        if ds.union(u, v):
            count += 1
            if count == n - s:
                return weight
    return -1

def main():
    while True:
        try:
            line = input().strip()
            if line == "":
                continue
            data = list(map(int, line.split()))
            s, p = data[0], data[1]
            outposts = [tuple(map(int, input().split())) for _ in range(p)]
            edges = []
            for i in range(p):
                for j in range(i + 1, p):
                    edges.append((distance(outposts[i], outposts[j]), i, j))
            min_D = kruskal(edges, p, s)
            print("{:.2f}".format(min_D))
        except EOFError:
            break

if __name__ == "__main__":
    main()
