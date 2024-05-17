def is_possible(m, a, b, c):
  """
  This function checks if it's possible for Alice, Bob, and Clara to pick menu items
  such that no item is picked by everyone.

  Args:
      m: Total number of items on the menu (1 <= m <= 100,000).
      a: Number of items Alice picks (1 <= a <= m).
      b: Number of items Bob picks (1 <= b <= m).
      c: Number of items Clara picks (1 <= c <= m).

  Returns:
      "possible" if it's possible, "impossible" otherwise.
  """
  
  # Check for the impossible cases:
  # - Total picks exceed menu items.
  if a + b + c > m:
    return "impossible"
  # - Everyone picks the entire menu (same number of picks as menu items).
  if a == b == c == m:
    return "impossible"

  # Minimum number of items everyone picks (could be 0).
  min_overlap = min(a, b, c)
  
  # If the total number of items picked minus minimum overlap is less than menu items,
  # it's possible to avoid picking something by everyone.
  return "possible" if (a + b + c - min_overlap) < m else "impossible"

# Read input from user
m, a, b, c = map(int, input().split())

# Call the function and print the result
result = is_possible(m, a, b, c)
print(result)
