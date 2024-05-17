#! /usr/bin/python3

from collections import defaultdict


def bfs(graph, start):
  """
  Performs Breadth-First Search from a starting node.

  Args:
      graph: A dictionary representing the directed graph.
      start: The starting node for the BFS traversal.

  Returns:
      A set containing all nodes reachable from the starting node.
  """
  visited = set()
  queue = [start]
  while queue:
    current = queue.pop(0)
    if current not in visited:
      visited.add(current)
      queue.extend(graph[current])
  return visited


def find_min_pages(chapters, dependencies):
  """
  Finds the minimum number of pages to read for two Culminating Concept chapters.

  Args:
      chapters: A list containing the number of pages for each chapter.
      dependencies: A list of tuples representing chapter dependencies.

  Returns:
      The minimum number of pages to read for two Culminating Concept chapters.
  """
  # Create a directed graph to represent chapter dependencies
  graph = defaultdict(list)
  for a, b in dependencies:
    graph[a].append(b)

  # Find in-degrees (number of incoming edges) for each chapter
  in_degrees = defaultdict(int)
  for _, b in dependencies:
    in_degrees[b] += 1  # Increment in-degree for dependent chapters

  # Identify Culminating Concept chapters (no incoming edges)
  culminating_chapters = set(chapter for chapter in range(1, len(chapters) + 1) if in_degrees[chapter] == 0)

  # Find connected components using BFS
  connected_components = set()
  for node in range(1, len(chapters) + 1):
    if node not in connected_components:
      component = bfs(graph, node)
      connected_components.update(component)

  # Find the minimum pages for two Culminating Concept chapters
  min_pages = float('inf')
  for component in connected_components:
    culminating_count = len(component.intersection(culminating_chapters))
    if culminating_count >= 2:
      total_pages = sum(chapters[chapter - 1] for chapter in component)
      min_pages = min(min_pages, total_pages)

  return min_pages


# Read input
num_chapters, num_dependencies = map(int, input().split())
chapters = list(map(int, input().split()))
dependencies = [tuple(map(int, input().split())) for _ in range(num_dependencies)]

# Find minimum pages
min_pages = find_min_pages(chapters, dependencies)

# Print output
print(min_pages)
