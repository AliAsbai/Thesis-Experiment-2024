from collections import defaultdict

def min_movements(n, m, labs, dependencies):
  """
  Finds the minimum number of painting movements for conservation stages,
  or returns -1 if no valid order exists due to cycles.

  Args:
      n: Number of conservation stages.
      m: Number of dependencies between stages.
      labs: List of integers (1 or 2) indicating the lab for each stage.
      dependencies: List of pairs (i, j) representing dependencies.

  Returns:
      The minimum number of painting movements, or -1 if no valid order exists.
  """
  # Initialize in-degree (number of dependencies) for each stage.
  in_degree = defaultdict(int)
  for i, j in dependencies:
    in_degree[j] += 1

  # Track current lab and processed stages for each lab.
  current_lab = labs[0]
  processed_per_lab = {1: 0, 2: 0}

  # Use topological sort approach with a set to track visited stages.
  queue = [i for i in range(n) if in_degree[i] == 0]
  visited = set()  # Track visited stages to avoid revisiting for cycle detection

  while queue:
    stage = queue.pop(0)
    current_lab = labs[stage]

    # Check if processing this stage creates a cycle:
    # If stage has already been visited and it's in a different lab, cycle exists.
    if stage in visited and current_lab != labs[stage]:
      return -1

    visited.add(stage)
    processed_per_lab[current_lab] += 1  # Mark stage processed for current lab

    # Decrement in-degree of dependent stages and add them to queue if ready.
    for dependent in dependencies:
      if dependent[0] == stage:
        in_degree[dependent[1]] -= 1
        if in_degree[dependent[1]] == 0:
          queue.append(dependent[1])

  # Check if all stages are processed.
  if sum(processed_per_lab.values()) != n:
    return -1  # Not all stages processed, implies cycle

  # Calculate minimum movements based on lab changes.
  movements = 0
  for i in range(1, n):
    if labs[i] != current_lab:
      movements += 1
      current_lab = labs[i]

  return movements

def main():
  t = int(input())
  for _ in range(t):
    n, m = map(int, input().split())
    labs = list(map(int, input().split()))
    dependencies = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    movements = min_movements(n, m, labs, dependencies)
    if movements == -1:
      print("No valid order exists")
    else:
      print(movements)

if __name__ == "__main__":
  main()
