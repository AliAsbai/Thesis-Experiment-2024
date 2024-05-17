def find_secret_code(numbers):
  """
  Finds the smallest integer c such that raising each number in the list to the c-th power
  results in an ending that matches the original number.

  Args:
      numbers: A list of integers representing the numbers formed by each group of Unown.

  Returns:
      The secret code (smallest integer c) or -1 if no such code exists.
  """
  # Find the maximum number of digits in any number.
  max_digits = len(str(max(numbers)))

  # Check for numbers ending in 0 - no code exists.
  if any(num % 10 == 0 for num in numbers):
    return -1

  # Iterate through potential code values (starting from 2).
  for code in range(2, max_digits + 1):
    valid = True
    # Check if each number raised to the power of code ends with the same digits.
    for num in numbers:
      last_digit = num % 10  # Only check the last digit
      if last_digit != num % (10**code):
        valid = False
        break
    if valid:
      return code

  # No code found.
  return -1

# Get input
n = int(input())
numbers = [int(x) for x in input().split()]

# Find and print the secret code.
secret_code = find_secret_code(numbers)
print(secret_code)
