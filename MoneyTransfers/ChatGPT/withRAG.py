import sys
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    graph = {}
    n, p, x, y = map(int, input().split())
    for _ in range(p):
        a, b, c = map(int, input().split())
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = c
        graph[b][a] = c
    
    m = int(input())
    swerc_banks = set(map(int, input().split()))

    # Apply Dijkstra's algorithm from X and Y
    distances_from_x = dijkstra(graph, x)
    distances_from_y = dijkstra(graph, y)

    # Check if SWERC owns all banks
    if swerc_banks.issuperset({x, y}):
        # If there's a direct connection between X and Y
        if y in graph[x]:
            print(graph[x][y])
            return
        else:
            print("Impossible")
            return

    min_total_cost = float('inf')
    impossible = True

    # Iterate through partnerships to find the minimum total cost
    for a in swerc_banks:
        for b in swerc_banks:
            if a != b and a in distances_from_x and b in distances_from_y:
                total_cost = distances_from_x[a] + graph[a].get(b, float('inf')) + distances_from_y[b]
                min_total_cost = min(min_total_cost, total_cost)
                impossible = False

    if impossible:
        print("Impossible")
    else:
        print(min_total_cost)

if __name__ == "__main__":
    main()
