#! /usr/bin/python3

def solve(m, n, p, q):
  """
  Finds the smallest m-digit number satisfying the given multiplication property.

  Args:
      m: Number of digits in the original number.
      n: Number of digits to cross out at the beginning.
      p: Number to append after remaining digits.
      q: Multiplier.

  Returns:
      The smallest m-digit number satisfying the property, or "IMPOSSIBLE" if none exists.
  """
  # Check if valid input (m >= n, non-zero digits).
  if m < n or not p or not q or not (str(p)[0] != '0' and str(q)[0] != '0'):
    return "IMPOSSIBLE"

  # Iterate through possible leading digits (avoid 0).
  for leading_digit in range(1, 10):
    # Construct the number string with leading digit and remaining digits (m-n).
    number_str = str(leading_digit) + ("0" * (m - n - 1))

    # Convert p (possibly multi-digit) to a string.
    p_str = str(p)

    # Simulate multiplication by q digit by digit.
    carry = 0
    for digit in reversed(str(q)):
      digit_int = int(digit)
      product = digit_int * int(number_str[0]) + carry
      # Update number_str with unit digit of product
      number_str = str(product % 10) + number_str[1:]
      # Update carry considering product's tens digit
      carry = product // 10

    # Check if multiplication and appending p results in the original number (consider carry in final comparison)
    original_number = int(leading_digit * 10**(m - 1)) + carry
    if number_str + p_str == str(original_number):
      return number_str

  # No solution found.
  return "IMPOSSIBLE"

# Read input from stdin.
m, n, p, q = map(int, input().split())

# Solve and print output.
result = solve(m, n, p, q)
print(result)
