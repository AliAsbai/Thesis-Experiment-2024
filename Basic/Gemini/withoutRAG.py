def is_valid_ada_constant(constant):
  """
  Checks if the given string is a valid Ada integer constant.

  Args:
      constant: The string to be evaluated.

  Returns:
      "yes" if the constant is valid, "no" otherwise.
  """

  # Check for empty string
  if not constant:
    return "no"

  # Split the constant based on the base identifier (e.g., "#")
  parts = constant.split("#", 1)

  # Check if base is present
  if len(parts) == 1:
    # Decimal constant
    try:
      int(constant)
      return "yes"
    except ValueError:
      return "no"
  else:
    # Base constant
    try:
      base = int(parts[0])
      if not (2 <= base <= 16):
        return "no"

      # Check for valid digits in the base (including uppercase letters)
      valid_digits = set("0123456789ABCDEF".lower())
      for digit in parts[1]:
        if digit not in valid_digits:
          return "no"

      # Check for leading/trailing whitespace and extra characters
      trimmed_digits = parts[1].strip()
      if not trimmed_digits or trimmed_digits != parts[1]:
        return "no"

      int(trimmed_digits, base)  # Check conversion without errors
      return "yes"
    except ValueError:
      return "no"

# Read the number of test cases
n = int(input())

# Loop through each test case
for _ in range(n):
  constant = input()
  print(is_valid_ada_constant(constant))
