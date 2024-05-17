#! /usr/bin/python3


def solve_case(n, m, labs, dependencies):
  """
  Solves a single test case for the minimum painting transportation count.

  Args:
      n: Number of conservation stages.
      m: Number of dependencies.
      labs: List of integers denoting lab for each stage (1 or 2).
      dependencies: List of pairs (i, j) representing dependencies between stages.

  Returns:
      The minimum number of painting transports required.
  """
  # Track stages completed in each lab
  lab1_completed = set()
  lab2_completed = set()
  transports = 0
  current_lab = labs[0]  # Start in the lab of the first stage

  # Process dependencies
  for i, j in dependencies:
    if labs[i] == labs[j]:  # Dependency within the same lab
      if labs[i] == 1:
        lab1_completed.add(i)
      else:
        lab2_completed.add(i)

  # Iterate through stages
  for i in range(n):
    # Check if stage needs to be processed based on lab and dependencies
    if labs[i] == 1 and i not in lab1_completed:
      continue
    if labs[i] == 2 and i not in lab2_completed:
      continue

    if labs[i] != current_lab:
      transports += 1
      current_lab = labs[i]

    # Mark stage as completed in its respective lab
    if labs[i] == 1:
      lab1_completed.add(i)
    else:
      lab2_completed.add(i)

  return transports


def main():
  """
  Reads input, solves each test case, and prints the results.
  """
  t = int(input())
  for _ in range(t):
    n, m = map(int, input().split())
    labs = list(map(int, input().split()))
    dependencies = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    result = solve_case(n, m, labs, dependencies)
    print(result)


if __name__ == "__main__":
  main()
