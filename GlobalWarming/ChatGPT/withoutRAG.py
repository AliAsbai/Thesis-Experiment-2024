def arrange_groups(graph, n):
    min_co2 = float('inf')
    
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j in graph[i]:
                for k in range(1, n+1):
                    if k != i and k != j and k in graph[i] and k in graph[j]:
                        co2 = graph[i][j] + graph[i][k]
                        min_co2 = min(min_co2, co2)
    
    return min_co2 if min_co2 != float('inf') else "impossible"

def main():
    n, m = map(int, input().split())
    graph = {i: {} for i in range(1, n + 1)}

    for _ in range(m):
        p, q, c = map(int, input().split())
        graph[p][q] = c
        graph[q][p] = c

    result = arrange_groups(graph, n)
    print(result)


if __name__ == "__main__":
    main()
