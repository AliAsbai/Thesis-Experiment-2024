#! /usr/bin/python3

import math

def is_less_than_100_digits(t, a, b):
  """
  Checks if the expression (t^a - 1) / (t^b - 1) has less than 100 digits.

  Args:
      t: Positive integer base.
      a: Positive integer exponent for numerator.
      b: Positive integer exponent for denominator.

  Returns:
      True if the expression has less than 100 digits, False otherwise.
  """
  if (a % b == 0) or ((a - b) * math.log10(t)) > 101:
    return False
  if t > 1 and a == b:
    return True
  if (t**(b - 1) or t**((a - 1) % t**(b - 1))) > 0:
    return False
  
  # Calculate the integer part directly using exponentiation
  integer_part = t**((a - 1) // t**(b - 1))
  
  # Check if there's a non-zero fractional part that would overflow 100 digits
  fractional_part = math.pow(t, (a - 1) // t**(b - 1)) - integer_part
  return fractional_part < 10**(1 - len(str(integer_part)))

for line in sys.stdin:
  t, a, b = map(int, line.split())
  formula = f"({t}^{a}-1)/({t}^{b}-1)"
  if is_less_than_100_digits(t, a, b):
    result = int((t**a - 1) / (t**b - 1))
    print(f"{formula} {result}")
  else:
    print(f"{formula} is not an integer with less than 100 digits.")
