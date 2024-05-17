from collections import defaultdict, deque

def bfs(graph, start, pages):
    visited = set()
    total_pages = pages[start]

    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                total_pages += pages[neighbor]
                queue.append(neighbor)

    return total_pages

def main():
    graph = defaultdict(list)

    # Read input
    n, m = map(int, input().split())
    pages = list(map(int, input().split()))
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    # Find Culminating Concept chapters
    culminating_concepts = set()
    for i in range(1, n + 1):
        if not graph[i]:
            culminating_concepts.add(i)

    # Find the two smallest Culminating Concept chapters
    cc_pages = []
    for culminating_chapter in culminating_concepts:
        total_pages = bfs(graph, culminating_chapter, pages)
        cc_pages.append(total_pages)

    cc_pages.sort()
    min_pages = sum(cc_pages[:2])

    print(min_pages)

if __name__ == "__main__":
    main()
