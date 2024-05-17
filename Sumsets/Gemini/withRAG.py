#! /usr/bin/python3

def find_largest_d(numbers):
  """
  Finds the largest d such that a + b + c = d where a, b, c and d are distinct elements of numbers.

  Args:
      numbers: A list of distinct integers.

  Returns:
      The largest d if found, otherwise "no solution".
  """

  # Sort the numbers in descending order
  numbers.sort(reverse=True)

  # Iterate through each element (d)
  for i in range(len(numbers)):
    # Check for pairs (a, b) that sum to d or subtract to d (avoid duplicates)
    for j in range(i + 1, len(numbers)):
      # Check for sum (avoid duplicates)
      if numbers[i] == numbers[j] + abs(numbers[i] - numbers[j]):
        if i != numbers.index(abs(numbers[i] - numbers[j])):
          return numbers[i]
      # Check for difference (avoid duplicates)
      elif abs(numbers[i] - numbers[j]) in numbers and i != numbers.index(abs(numbers[i] - numbers[j])):
        return numbers[i]

  # No solution found
  return "no solution"

# Read input
n = int(input())
numbers = []
for _ in range(n):
  numbers.append(int(input()))

# Find and print the largest d
largest_d = find_largest_d(numbers)
print(largest_d)
