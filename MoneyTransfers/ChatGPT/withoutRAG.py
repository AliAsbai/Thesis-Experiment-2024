import heapq

def dijkstra(graph, start, end):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances[end]

def cheapest_transfer(N, P, X, Y, partnerships, M, swerc_banks):
    # Create graph with transfer fees
    graph = {i: {} for i in range(1, N + 1)}
    for a, b, c in partnerships:
        graph[a][b] = c
        graph[b][a] = c

    # Calculate the cheapest transfer fee without SWERC banks
    cheapest_fee = dijkstra(graph, X, Y)

    # Check if SWERC banks are directly connected
    for a in swerc_banks:
        for b in swerc_banks:
            if a != b and b in graph[a]:
                return "Infinity"

    # Iterate through different fees to find the maximum fee for SWERC to provide the cheapest transfer
    max_fee = 0
    for fee in range(1, 101):  # Iterate from 1 to 100 as per the problem constraints
        # Update the graph with the fee for SWERC banks
        for a in swerc_banks:
            for b in swerc_banks:
                if a != b:
                    graph[a][b] = graph[b][a] = fee

        # Calculate the transfer fee with SWERC involvement
        transfer_fee = dijkstra(graph, X, Y)
        
        # Check if SWERC can provide the cheapest transfer
        if transfer_fee > cheapest_fee:
            max_fee = max(max_fee, fee)

    if max_fee == 0:
        return "Impossible"
    else:
        return max_fee

# Sample input
N, P, X, Y = map(int, input().split())
partnerships = [tuple(map(int, input().split())) for _ in range(P)]
M = int(input())
swerc_banks = list(map(int, input().split()))

# Output result
result = cheapest_transfer(N, P, X, Y, partnerships, M, swerc_banks)
print(result)
