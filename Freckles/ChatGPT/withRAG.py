import sys
import math
import heapq

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root == y_root:
            return False
        
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        
        return True

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def kruskal(freckles):
    n = len(freckles)
    distances = []
    
    for i in range(n):
        for j in range(i + 1, n):
            distances.append((distance(freckles[i], freckles[j]), i, j))
    
    distances.sort()
    
    total_distance = 0
    ds = DisjointSet(n)
    num_components = n
    
    for dist, u, v in distances:
        if ds.union(u, v):
            total_distance += dist
            num_components -= 1
            if num_components == 1:
                break
    
    return total_distance

for line in sys.stdin:
    cases = int(line.strip())
    for _ in range(cases):
        input()  # Blank line
        n = int(input())
        freckles = []
        for _ in range(n):
            x, y = map(float, input().split())
            freckles.append((x, y))
        print("{:.2f}".format(kruskal(freckles)))
        print()  # Blank line
