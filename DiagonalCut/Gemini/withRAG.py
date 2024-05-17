#! /usr/stdin/python3

def count_cut_blocks(M, N):
  """Calculates the number of blocks cut in half diagonally."""
  # Minimum number of cuts to reach the other corner
  cuts = min(M - 1, N - 1)

  # Count only the diagonal cuts that go through the center block
  # (assuming blocks are of unit size)
  return min(cuts, max(0, (M + N - 2) // 2 - 1))

# Read input
M, N = map(int, input().split())

# Calculate number of cut blocks
cut_blocks = count_cut_blocks(M, N)

# Print the result
print(cut_blocks)
