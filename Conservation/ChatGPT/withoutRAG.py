from collections import defaultdict, deque

def topological_sort(graph, indegree):
    order = []
    queue = deque()

    for node in range(1, len(indegree)):
        if indegree[node] == 0:
            queue.append(node)

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order

def min_transports(n, m, labs, dependencies):
    graph = defaultdict(list)
    indegree = [0] * (n + 1)

    for dep in dependencies:
        graph[dep[0]].append(dep[1])
        indegree[dep[1]] += 1

    order = topological_sort(graph, indegree)

    transports = 0
    lab1, lab2 = labs[0], 3 - labs[0]
    for stage in order:
        if labs[stage - 1] == lab1:
            lab1, lab2 = lab2, lab1
            transports += 1

    return transports

# Reading input
T = int(input().strip())

for _ in range(T):
    n, m = map(int, input().split())
    labs = list(map(int, input().split()))
    dependencies = [tuple(map(int, input().split())) for _ in range(m)]

    result = min_transports(n, m, labs, dependencies)
    print(result)
