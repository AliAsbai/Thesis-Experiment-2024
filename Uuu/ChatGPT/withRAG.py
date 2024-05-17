import sys

def generate_slow_graph(N, M):
    edges = []
    # Create a connected graph with one connected component
    for i in range(1, N):
        edges.append((i, i+1))
    # Add remaining edges to satisfy the edge count
    for i in range(M - (N - 1)):
        edges.append((i % N + 1, (i + 1) % N + 1))
    return edges

def main():
    for line in sys.stdin:
        N, M = map(int, line.split())
        edges = generate_slow_graph(N, M)
        for edge in edges:
            print(edge[0], edge[1])

if __name__ == "__main__":
    main()
