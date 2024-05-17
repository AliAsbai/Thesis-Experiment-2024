import math

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

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    total_length = 0
    for u, v, weight in edges:
        if uf.union(u, v):
            total_length += weight
    return total_length

def main():
    num_cases = int(input())
    input()  # Ignore the blank line

    for _ in range(num_cases):
        n = int(input())
        freckles = []
        for _ in range(n):
            x, y = map(float, input().split())
            freckles.append((x, y))

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((i, j, distance(freckles[i], freckles[j])))

        total_ink_length = kruskal(edges, n)
        print("{:.2f}".format(total_ink_length))

        if _ < num_cases - 1:
            print()

if __name__ == "__main__":
    main()
