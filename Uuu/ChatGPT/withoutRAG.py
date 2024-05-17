def main():
    N, M = map(int, input().split())

    # Generate a chain-like graph
    edges = [(i, i+1) for i in range(1, N)]

    # Add additional edges connecting the start and end vertices of the chain
    additional_edges = M - (N - 1)
    for i in range(1, additional_edges + 1):
        edges.append((1, N))

    # Output the edges
    for edge in edges:
        print(edge[0], edge[1])

if __name__ == "__main__":
    main()
