import math

class DisjointSet:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def kruskal(S, P, outposts):
    edges = []
    for i in range(P):
        for j in range(i+1, P):
            edges.append((i, j, distance(outposts[i], outposts[j])))
    edges.sort(key=lambda x: x[2])

    dsu = DisjointSet(P)
    satellite_connected = 0
    for s in S:
        satellite_connected += dsu.union(0, s)

    min_d = 0
    for u, v, d in edges:
        if dsu.union(u, v):
            min_d = max(min_d, d)
            if satellite_connected == P - 1:
                break

    return min_d

def main():
    N = int(input().strip())  # Number of test cases
    for _ in range(N):
        S, P = map(int, input().split())  # Number of satellite channels, Number of outposts
        outposts = [tuple(map(int, input().split())) for _ in range(P)]
        min_d = kruskal(set(map(int, input().split())), P, outposts)
        print("{:.2f}".format(min_d))

if __name__ == "__main__":
    main()
