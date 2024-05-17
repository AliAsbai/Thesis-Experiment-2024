def reverse_binary(n):
  """Reverses the binary representation of an integer and returns the corresponding integer.

  Args:
      n: The integer to be reversed.

  Returns:
      The integer obtained by reversing the binary representation of n.
  """
  # Convert the integer to binary string (without the '0b' prefix)
  binary_str = bin(n)[2:]

  # Reverse the binary string
  reversed_binary = binary_str[::-1]

  # Convert the reversed binary string back to integer (base 2)
  reversed_number = int(reversed_binary, 2)

  return reversed_number

# Get user input
number = int(input())

# Reverse the binary representation and print the result
reversed_number = reverse_binary(number)
print(reversed_number)
