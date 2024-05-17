import sys
from collections import defaultdict
import heapq

def prim(graph):
    min_heap = [(0, 0)]  # (weight, node)
    visited = set()
    min_margin = float('-inf')

    while min_heap:
        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue
        
        visited.add(node)
        min_margin = max(min_margin, weight)

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    return min_margin

def min_margin(n, m, sensors):
    graph = defaultdict(list)

    for i in range(m):
        a, b, w = sensors[i]
        graph[a].append((b, w))
        graph[b].append((a, w))

    return prim(graph)

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        m = int(input().strip())
        sensors = []
        for _ in range(m):
            a, b, w = map(int, input().split())
            sensors.append((a, b, w))
        
        result = min_margin(n, m, sensors)
        print(result)

if __name__ == "__main__":
    main()
