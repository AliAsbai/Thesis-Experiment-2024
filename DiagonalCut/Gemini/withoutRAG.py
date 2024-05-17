def get_cut_pieces(m, n):
  """
  Calculates the number of chocolate pieces cut in half diagonally.

  Args:
      m: Number of blocks in a column (1 <= m <= 10^18).
      n: Number of blocks in a row (1 <= n <= 10^18).

  Returns:
      The number of chocolate pieces cut in half diagonally (modulo 10**9 + 7).
  """
  # Identify the shorter side (either m or n).
  shorter = min(m, n)

  # Calculate the number of diagonal cuts that will split blocks in half.
  cut_pieces = 0
  for i in range(1, shorter):
    # For each cut of length i, calculate the number of blocks it splits in half.
    cut_pieces = (cut_pieces + min(n - i, m - i)) % (10**9 + 7)  # Modulo operation to avoid overflow

  return cut_pieces

# Read input
m, n = map(int, input().split())

# Calculate and print the result (modulo 10**9 + 7)
cut_pieces = get_cut_pieces(m, n)
print(cut_pieces)
