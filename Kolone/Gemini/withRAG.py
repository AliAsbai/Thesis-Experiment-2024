#! /usr/bin/python3

def swap(arr, i, j):
  """Swaps elements at indices i and j in the array arr."""
  arr[i], arr[j] = arr[j], arr[i]

def solve(n1, n2, arr, t):
  """
  Simulates the ant jumping scenario for T seconds and returns the final order.

  Args:
      n1: Number of ants in the first row.
      n2: Number of ants in the second row.
      arr: List containing all ants in their initial order.
      t: Number of seconds for simulation.
  """
  total_ants = n1 + n2
  for _ in range(t):
    swap_indices = []
    for i in range(n1, total_ants):
      if (i > 0 and arr[i] in arr[:n1] and arr[i-1] in arr[n1:]):
        swap_indices.append(i)
    for i in swap_indices:
      swap(arr, i, i-1)

  # Return the final order of ants
  return "".join(arr)

# Read input
n1, n2 = map(int, input().split())
arr1 = list(input())
arr2 = list(input())
t = int(input())

# Combine ants and call the solve function
all_ants = arr1 + arr2
final_order = solve(n1, n2, all_ants, t)

# Print the final order
print(final_order)
