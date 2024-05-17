def count_hamiltonian_cycles(graph, forbidden_edges):
    n = len(graph)
    dp = [[0] * (1 << n) for _ in range(n)]
    for i in range(n):
        dp[i][1 << i] = 1
    
    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if graph[u][v] and (mask & (1 << v)) and (u, v) not in forbidden_edges and (v, u) not in forbidden_edges:
                    dp[v][mask] += dp[u][mask ^ (1 << v)]
    
    total_cycles = 0
    for u in range(n):
        if graph[u][0] and (u, 0) not in forbidden_edges and (0, u) not in forbidden_edges:
            total_cycles += dp[u][(1 << n) - 1]
    
    return total_cycles % 9901

def main():
    T = int(input().strip())
    for case in range(1, T + 1):
        n, k = map(int, input().strip().split())
        graph = [[0] * n for _ in range(n)]
        forbidden_edges = set()
        for _ in range(k):
            u, v = map(int, input().strip().split())
            u -= 1
            v -= 1
            graph[u][v] = graph[v][u] = 1
            forbidden_edges.add((u, v))
            forbidden_edges.add((v, u))
        
        result = count_hamiltonian_cycles(graph, forbidden_edges)
        print("Case #{}: {}".format(case, result))

if __name__ == "__main__":
    main()
