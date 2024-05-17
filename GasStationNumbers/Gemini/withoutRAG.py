def next_highest_price(price):
  """
  Finds the next highest price that can be displayed using the same digits.

  Args:
      price: A string representing the current price with a decimal point.

  Returns:
      A string representing the next highest price or "The price cannot be raised".
  """
  digits = list(price.split(".")[0])  # Separate digits without decimal
  decimal = price.split(".")[1]  # Get the decimal part

  # Remove leading zeros (except for single leading zero)
  if len(digits) > 1 and digits[0] == "0":
    digits = digits[1:]

  # Handle cases where all digits are the same or no digit can be flipped
  if all(d == digits[0] for d in digits):
    return "The price cannot be raised"

  # Find the first digit (from right) that can be flipped
  i = len(digits) - 2
  while i >= 0 and digits[i] >= digits[i + 1]:
    i -= 1

  # If no digit can be flipped, price cannot be raised
  if i < 0:
    return "The price cannot be raised"

  # Find the smallest digit greater than the chosen digit (i) on the right side
  j = len(digits) - 1
  while j > i and digits[j] <= digits[i]:
    j -= 1

  # Swap digits
  digits[i], digits[j] = digits[j], digits[i]

  # Reverse digits from position after i (inclusive) to the end
  digits[i + 1:] = digits[i + 1:][::-1]

  # Add leading zero back if necessary
  if price.startswith("0") and len(digits) > 1:
    digits.insert(0, "0")

  return f"{''.join(digits)}.{decimal}"

# Read input until a line with just a decimal point is encountered
while True:
  price = input()
  if price == ".":
    break
  result = next_highest_price(price)
  print(result)
