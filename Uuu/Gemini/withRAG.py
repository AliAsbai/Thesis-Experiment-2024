#! /usr/bin/python3

import random

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Bug: Should be xroot != yroot to avoid unnecessary merging
    if xroot == yroot:
        return

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def main():
    n, m = map(int, input().split())

    # Create parent and rank arrays for union-find
    parent = list(range(n))
    rank = [0] * n

    # Intentionally create a single long chain for slow merging
    for i in range(1, n):
        union(parent, rank, i-1, i)

    # Targeted connections: connect every other node to the last node
    for i in range(1, n, 2):
        union(parent, rank, i, n-1)

    # Generate remaining edges (less important for this approach)
    for _ in range(m - n + 1):
        u = random.randint(0, n-2)
        v = random.randint(u + 1, n-1)
        print(u + 1, v + 1)

if __name__ == "__main__":
    main()
