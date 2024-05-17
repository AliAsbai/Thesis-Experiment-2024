def arrange_numbers(numbers, order):
  """
  Rearranges three numbers in the desired order.

  Args:
      numbers: A list of three integers (A, B, and C).
      order: A string representing the desired order (ABC, ACB, etc.).

  Returns:
      A string containing the rearranged numbers separated by spaces.
  """
  # Sort the numbers for reliable mapping
  numbers.sort()
  mapping = {"A": numbers[0], "B": numbers[1], "C": numbers[2]}
  return " ".join([str(mapping[char]) for char in order])

# Get input
numbers = [int(x) for x in input().split()]
order = input()

# Rearrange and print
result = arrange_numbers(numbers, order)
print(result)
