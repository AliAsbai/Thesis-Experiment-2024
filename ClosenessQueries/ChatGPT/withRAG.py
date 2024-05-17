import sys
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bidirectional_bfs(self, start, end):
        if start == end:
            return 0

        forward_visited = [False] * self.vertices
        backward_visited = [False] * self.vertices
        forward_queue = deque()
        backward_queue = deque()

        forward_queue.append((start, 0))
        backward_queue.append((end, 0))
        forward_visited[start] = True
        backward_visited[end] = True

        while forward_queue and backward_queue:
            forward_node, forward_dist = forward_queue.popleft()
            backward_node, backward_dist = backward_queue.popleft()

            for neighbor in self.graph[forward_node]:
                if not forward_visited[neighbor]:
                    forward_visited[neighbor] = True
                    forward_queue.append((neighbor, forward_dist + 1))

                if backward_visited[neighbor]:
                    return forward_dist + backward_dist + 1

            for neighbor in self.graph[backward_node]:
                if not backward_visited[neighbor]:
                    backward_visited[neighbor] = True
                    backward_queue.append((neighbor, backward_dist + 1))

                if forward_visited[neighbor]:
                    return forward_dist + backward_dist + 1

        return -1

def main():
    N, M = map(int, input().split())
    graph = Graph(N)
    
    for _ in range(M):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    Q = int(input())
    for _ in range(Q):
        u, v = map(int, input().split())
        print(graph.bidirectional_bfs(u, v))

if __name__ == "__main__":
    main()
