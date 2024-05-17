from math import log2

def calculate_tape(n, sheets):
  """
  Calculates the minimum tape needed to make an A1 paper.

  Args:
      n: The A-size of the smallest paper (2 <= n <= 30).
      sheets: A list of integers (n-1 length) representing the number of sheets of each size (A2 to An).

  Returns:
      A float representing the minimum tape length needed, or "impossible" if insufficient paper.
  """
  # Calculate area required for A1 paper
  a1_area = 2 ** (-5/4)

  # Calculate area of each paper size
  paper_areas = [a1_area * 2 ** (-i * (5/4)) for i in range(n - 1, 0, -1)]
  paper_areas.append(a1_area)  # Add A1 size

  # Calculate total area available from sheets
  total_area = 0
  for i in range(n - 1):
    total_area += paper_areas[i] * sheets[i]

  # Check if enough paper
  if total_area < a1_area:
    return "impossible"

  # Calculate tape needed for each paper combination
  tape_lengths = []
  for i in range(1, n):
    # Calculate number of sheets needed from current size
    sheets_needed = int(ceil((a1_area - total_area) / paper_areas[i]))
    # Check if enough sheets available
    if sheets_needed > sheets[i - 1]:
      return "impossible"
    # Calculate tape length for this combination
    tape_lengths.append(sheets_needed * paper_areas[i - 1])
    # Update total area with used sheets
    total_area += sheets_needed * paper_areas[i]

  # Return minimum tape length
  return min(tape_lengths)

def ceil(x):
  """
  Custom ceiling function for floating point numbers.
  """
  return int(x - 0.000000001) if x > int(x) else int(x)

# Read input
n = int(input())
sheets = list(map(int, input().split()))

# Calculate and print result
result = calculate_tape(n, sheets)
print(result)
