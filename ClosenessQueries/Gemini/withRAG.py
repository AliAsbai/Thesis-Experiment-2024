#! /usr/bin/python3

from collections import defaultdict


class DisjointSet:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parents[u] != u:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return

        if self.rank[root_u] > self.rank[root_v]:
            self.parents[root_v] = root_u
        else:
            self.parents[root_u] = root_v
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_v] += 1


def bfs(graph, start, target):
    visited = set()
    queue = [(start, 0)]

    while queue:
        node, distance = queue.pop(0)
        if node == target:
            return distance
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append((neighbor, distance + 1))
    return -1


def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    q = int(input())
    disjoint_set = DisjointSet(n)

    for _ in range(q):
        u, v = map(int, input().split())
        root_u = disjoint_set.find(u)
        root_v = disjoint_set.find(v)

        # Check for disconnected graphs
        if root_u != root_v:
            print(-1)
            continue

        distance = bfs(graph, u, v)
        print(distance)


if __name__ == "__main__":
    solve()
