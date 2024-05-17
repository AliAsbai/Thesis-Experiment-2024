#! /usr/bin/python3

def build_prefix_sum(memory):
  """Creates a prefix sum array where each element represents the total number of 1s before its index."""
  prefix_sum = [0] * (len(memory) + 1)  # Add padding for easier calculations
  for i in range(len(memory)):
    prefix_sum[i + 1] = prefix_sum[i] + memory[i]
  return prefix_sum

def count_bits(prefix_sum, l, r):
  """Calculates the number of 1s between l and r using prefix sums."""
  return prefix_sum[r + 1] - prefix_sum[l]  # Adjust for 0-based indexing

def main():
  """Reads input, simulates memory operations with prefix sums, and prints results."""
  N, K = map(int, input().split())
  memory = [0] * N  # Initialize memory with all bits set to 0
  prefix_sum = build_prefix_sum(memory)

  for _ in range(K):
    query = input().split()
    if query[0] == "F":
      i = int(query[1]) - 1  # Adjust for 0-based indexing
      memory[i] = 1 - memory[i]  # Flip the bit at index i
      # Update prefix sum based on the change (0 to 1 or 1 to 0)
      prefix_sum[i + 1] += memory[i] - (1 - memory[i])
    else:
      l, r = map(int, query[1:])
      count = count_bits(prefix_sum, l, r)
      print(count)

if __name__ == "__main__":
  main()
