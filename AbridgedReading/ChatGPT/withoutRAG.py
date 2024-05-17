from collections import defaultdict

# Function to perform depth-first search to calculate total pages
def dfs(graph, node, pages, visited):
    # If node is already visited, return 0
    if node in visited:
        return 0
    # Mark node as visited
    visited.add(node)
    # Calculate total pages for current node including its prerequisites
    total_pages = pages[node - 1]
    for neighbor in graph[node]:
        total_pages += dfs(graph, neighbor, pages, visited)
    return total_pages

# Function to calculate minimum pages required for two culminating concept chapters
def calculate_min_pages(chapters, dependencies, pages):
    graph = defaultdict(list)

    # Construct graph from dependencies
    for dependency in dependencies:
        a, b = dependency
        graph[b].append(a)  # Reverse the direction of edges

    min_pages = float('inf')

    # Iterate over all pairs of culminating concept chapters
    for i in range(1, chapters + 1):
        for j in range(i + 1, chapters + 1):
            # Check if both chapters are culminating concept chapters
            if i not in graph and j not in graph:
                total_pages = pages[i - 1] + pages[j - 1]
                visited = set()
                # Calculate total pages including prerequisites
                total_pages += dfs(graph, i, pages, visited)
                total_pages += dfs(graph, j, pages, visited)
                # Update minimum pages if needed
                min_pages = min(min_pages, total_pages)

    return min_pages

# Reading input
n, m = map(int, input().split())
pages = list(map(int, input().split()))

dependencies = [tuple(map(int, input().split())) for _ in range(m)]

# Calculating and printing the result
result = calculate_min_pages(n, dependencies, pages)
print(result)
