from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def bfs(self, start, end):
        visited = [False] * self.vertices
        distance = [-1] * self.vertices
        queue = deque()

        queue.append(start)
        visited[start] = True
        distance[start] = 0

        while queue:
            current = queue.popleft()

            for neighbor in self.adjacency_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[current] + 1
                    queue.append(neighbor)

                    if neighbor == end:
                        return distance[neighbor]

        return -1

# Input parsing
N, M = map(int, input().split())
graph = Graph(N)

for _ in range(M):
    u, v = map(int, input().split())
    graph.add_edge(u, v)

Q = int(input())

# Handle queries
for _ in range(Q):
    u, v = map(int, input().split())
    print(graph.bfs(u, v)))

