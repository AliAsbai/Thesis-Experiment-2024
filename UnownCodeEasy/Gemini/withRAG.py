#! /usr/bin/python3

def is_valid_code(numbers, code):
  """Checks if the given code works for all numbers."""
  for num in numbers:
    last_digits = num % 10**code
    # Handle numbers ending in 5 as a special case
    if num % 5 == 0 and code > 1 and last_digits % (5**(code-1)) != 0:
      return False
    elif num**code % 10**code != last_digits:
      return False
  return True

def find_secret_code(numbers):
  """Finds the smallest valid secret code for the given numbers."""
  for power in range(2, 21): # Maximum power of 20 for efficiency
    # Check powers of 2 and numbers formed by adding 1 to powers of 2
    for exp in range(power + 1):
      code = 2**exp
      if is_valid_code(numbers, code):
        return code
      if exp > 0 and is_valid_code(numbers, code + 1):
        return code + 1
  return -1

def main():
  """Reads input and outputs the secret code."""
  num_groups = int(input())
  numbers = [int(x) for x in input().split()]
  code = find_secret_code(numbers)
  print(code)

if __name__ == "__main__":
  main()
