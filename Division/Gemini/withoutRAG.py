def is_less_than_100_digits(num):
  """Checks if the absolute value of the number has less than 100 digits."""
  return len(str(abs(num))) < 100

def solve(t, a, b):
  """Calculates the formula and checks if the result has less than 100 digits."""
  numerator = str(pow(t, a) - 1)
  denominator = str(pow(t, b) - 1)
  if denominator == "0":
    return "is not an integer with less than 100 digits."

  # Check divisibility by comparing string lengths
  if len(numerator) > len(denominator):
    return "is not an integer with less than 100 digits."

  # Handle cases where numerator length is equal or less
  result_len = len(numerator) - len(denominator)
  if result_len < 0:
    return "is not an integer with less than 100 digits."
  elif result_len > 99:
    return "is not an integer with less than 100 digits."
  else:
    return f"({t}^{a}-1)/({t}^{b}-1) {numerator[:result_len]}"  # Slice result string

# Read input lines
for line in iter(input, ""):
  # Split the line into integers
  t, a, b = map(int, line.split())
  # Solve the case and print the output
  print(solve(t, a, b))
