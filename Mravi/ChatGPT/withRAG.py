import sys

def dfs(node, parent, graph, flow, superpowers, needed, L):
    if node not in graph:
        return L >= needed[node]
    
    total_flow = 0
    for child, percentage in graph[node]:
        if child == parent:
            continue
        if superpowers[(node, child)]:
            child_needed = needed[child] * percentage * percentage
        else:
            child_needed = needed[child] * percentage
        if not dfs(child, node, graph, flow, superpowers, needed, L * percentage):
            return False
        total_flow += child_needed
    
    return L >= total_flow

def main():
    graph = {}
    superpowers = {}
    
    # Read input
    lines = sys.stdin.readlines()
    N = int(lines[0].strip())
    for line in lines[1:N]:
        Ai, Bi, Xi, Ti = map(int, line.split())
        if Ai not in graph:
            graph[Ai] = []
        if Bi not in graph:
            graph[Bi] = []
        graph[Ai].append((Bi, Xi))
        graph[Bi].append((Ai, Xi))
        superpowers[(Ai, Bi)] = Ti
        superpowers[(Bi, Ai)] = Ti
    
    needed = list(map(float, lines[N].split()))
    
    # Binary search for minimum L
    low, high = 0, 2e9
    max_iterations = 1000
    tolerance = 1e-6
    iteration = 0
    while high - low > tolerance and iteration < max_iterations:
        mid = (low + high) / 2
        if dfs(1, -1, graph, {}, superpowers, needed, mid):
            high = mid
        else:
            low = mid
        iteration += 1
    
    print("{:.2f}".format(high))

if __name__ == "__main__":
    main()
