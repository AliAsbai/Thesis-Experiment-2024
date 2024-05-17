def swap_ants(row1, row2):
  """Swaps ants between two rows based on their direction."""
  new_row1, new_row2 = [], []
  for i in range(min(len(row1), len(row2))):
    if row1[i] != row2[i]:
      new_row1.append(row2[i])
      new_row2.append(row1[i])
    else:
      new_row1.append(row1[i])
      new_row2.append(row2[i])
  # Append remaining ants from the longer row (if any)
  new_row1.extend(row1[len(row2):])
  new_row2.extend(row2[len(row1):])
  return new_row1, new_row2

def simulate_jumps(row1, row2, t):
  """Simulates ant jumps for a given number of seconds."""
  for _ in range(t):
    row1, row2 = swap_ants(row1, row2[::-1])  # Reverse row2 for opposite direction
  return row1 + row2

def main():
  """Reads input, simulates jumps, and prints the final order."""
  n1, n2 = map(int, input().split())
  row1 = input()
  row2 = input()
  t = int(input())
  final_order = simulate_jumps(row1, row2, t)
  print("".join(final_order))

if __name__ == "__main__":
  main()
