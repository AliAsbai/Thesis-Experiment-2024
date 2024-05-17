#! /usr/bin/python3

def is_valid_digit(char):
  return char in "0125689"

def swap_digits(price, i, j):
  price_list = list(price)
  price_list[i], price_list[j] = price_list[j], price_list[i]
  return "".join(price_list)

def next_highest_price(price):
  # Handle single digit case
  if len(price) == 1:
    return "The price cannot be raised"

  # Find the decimal point
  decimal_index = price.find(".")
  
  # Separate integer and fractional parts (handling potential leading zero)
  integer_part = "0" + price[:decimal_index] if decimal_index > 0 else price
  fractional_part = price[decimal_index+1:] if decimal_index > 0 else ""

  # Find the first digit that can be incremented (treating 5 as 6 only at the end)
  i = len(integer_part) - 2
  while i >= 0 and (integer_part[i] == "9" or integer_part[i] == "5" and (i == 0 or integer_part[i+1] <= "2")):
    i -= 1

  # No digit can be incremented or only "5" left to increment (which can't be incremented at the end)
  if i == -1 or (integer_part[i] == "5" and len(integer_part) > 2 and integer_part[i+1] > "2"):
    return "The price cannot be raised"

  # Swap the digit with the one behind it, considering special case for "5" at the end
  if integer_part[i] == "5":
    new_integer_part = integer_part[:i] + "6" + integer_part[i+1:]
  else:
    new_integer_part = swap_digits(integer_part, i, i+1)
  
  # Sort the remaining digits (no need to treat 5 as 2 here)
  remaining_digits = new_integer_part[i+2:]
  sorted_digits = sorted(remaining_digits)
  new_integer_part = new_integer_part[:i+2] + "".join(sorted_digits)

  # Combine integer and fractional parts with decimal point
  new_price = new_integer_part + ("." + fractional_part if fractional_part else "")

  # Swap last two digits for proper formatting
  return new_price[::-1]

for line in iter(lambda: input(), ""):
  price = line.strip()
  if not price:
    break
  if not all(is_valid_digit(char) for char in price):
    print("Invalid input")
    continue
  result = next_highest_price(price)
  print(result)
