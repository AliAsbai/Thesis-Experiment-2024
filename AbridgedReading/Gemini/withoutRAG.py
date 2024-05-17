from collections import defaultdict

def min_pages_culminating(chapters, dependencies):
  """
  Calculates the minimum number of pages to read for two culminating chapters.

  Args:
      chapters: A list of integers representing the number of pages in each chapter.
      dependencies: A list of tuples (a, b) indicating chapter a is a prerequisite for b.

  Returns:
      The minimum number of pages to read for two culminating chapters, or -1 if no solution exists.
  """

  # Build a dependency dictionary to efficiently track prerequisite relationships.
  dependency_dict = defaultdict(list)
  for a, b in dependencies:
    dependency_dict[a].append(b)

  # Find all culminating chapters (no outgoing dependencies).
  culminating_chapters = [i for i, deps in dependency_dict.items() if not deps]

  # Handle the edge case where there are no culminating chapters.
  if not culminating_chapters:
    return -1  # No solution found

  # Perform a topological sort (BFS) to determine a valid reading order.
  # This ensures we read prerequisites before dependent chapters.
  visited = set()
  queue = collections.deque(culminating_chapters)
  reading_order = []

  while queue:
    chapter = queue.popleft()
    if chapter in visited:
      continue
    visited.add(chapter)
    reading_order.append(chapter)
    for prerequisite in dependency_dict[chapter]:
      if prerequisite not in visited:
        queue.append(prerequisite)

  # Calculate the minimum total pages for two culminating chapters.
  min_pages = float('inf')
  for i in range(len(reading_order) - 1):
    for j in range(i + 1, len(reading_order)):
      total_page_1 = total_pages(reading_order[i], chapters, dependency_dict)
      total_page_2 = total_pages(reading_order[j], chapters, dependency_dict)
      min_pages = min(min_pages, total_page_1 + total_page_2)

  return min_pages

def total_pages(chapter, chapters, dependency_dict):
  """
  Calculates the total number of pages required for a chapter and its prerequisites recursively.

  Args:
      chapter: The chapter number.
      chapters: A list of integers representing the number of pages in each chapter.
      dependency_dict: A dictionary mapping chapters to their prerequisite chapters.

  Returns:
      The total number of pages for the chapter and its prerequisites.
  """

  if chapter in visited:
    return visited[chapter]

  visited[chapter] = chapters[chapter - 1]  # Subtract 1 for indexing
  for dep in dependency_dict[chapter]:
    visited[chapter] += total_pages(dep, chapters, dependency_dict)
  return visited[chapter]

# Read input
n, m = map(int, input().split())
chapters = list(map(int, input().split()))
dependencies = [tuple(map(int, input().split())) for _ in range(m)]

# Solve and print result
result = min_pages_culminating(chapters, dependencies)
print(result)
