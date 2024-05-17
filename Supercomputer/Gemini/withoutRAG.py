def set_bit(memory, index):
  memory |= (1 << index)  # Set bit using bitwise OR

def clear_bit(memory, index):
  memory &= ~(1 << index)  # Clear bit using bitwise AND and NOT

def count_ones(memory, start, end):
  # Efficient bit counting using Brian Kernighan's algorithm
  count = 0
  mask = memory
  while mask:
    count += mask & 1
    mask >>= 1
  return count

def main():
  # ... (same as previous code)

  for _ in range(k):
    query = input().split()
    if query[0] == "F":
      index = int(query[1]) - 1
      if memory & (1 << index):
        clear_bit(memory, index)
      else:
        set_bit(memory, index)
    else:
      l, r = map(int, query[1:])
      result = count_ones(memory >> (l - 1), r - l + 1)  # Shift right to align with query range
      print(result)
