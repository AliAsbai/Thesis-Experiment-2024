MOD = 10**9 + 7

def count_inversions(sequence):
  """
  This function calculates the sum of inversions for all possible 0-1 sequences
  obtained by replacing '?' with '0' or '1'.

  Args:
      sequence: A string containing '0', '1', and '?'.

  Returns:
      The sum of inversions for all possible sequences (modulo MOD).
  """
  zeros, ones = 0, 0
  inversions = 0

  for char in sequence:
    if char == '0':
      inversions = (inversions + ones) % MOD  # Count inversions with existing ones
    elif char == '1':
      ones += 1
      # Inversions with potential future zeros based on leading '?'s
      inversions = (inversions + zeros * pow(2, sequence.count('?') - 1, MOD)) % MOD

  return inversions

# Read input string
sequence = input()

# Calculate and print the sum of inversions
print(count_inversions(sequence))
