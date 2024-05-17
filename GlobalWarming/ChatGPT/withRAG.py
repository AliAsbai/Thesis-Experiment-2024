import sys

class DisjointSet:
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

        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1

        return True

def main():
    # Read input
    for line in sys.stdin:
        n, m = map(int, line.split())
        break

    # Initialize disjoint-set data structure
    ds = DisjointSet(n)

    # Initialize variables
    total_co2 = 0
    edges = []

    # Read friendships and CO2 emissions
    for _ in range(m):
        p, q, c = map(int, input().split())
        p -= 1
        q -= 1
        edges.append((c, p, q))

    # Sort edges by CO2 emissions in ascending order
    edges.sort()

    # Iterate through sorted edges and join groups
    for c, p, q in edges:
        if ds.union(p, q):
            total_co2 += c

    # Check if all students are in one group
    root = ds.find(0)
    for i in range(1, n):
        if ds.find(i) != root:
            print("impossible")
            return

    # Output total CO2 emissions
    print(total_co2)

if __name__ == "__main__":
    main()
