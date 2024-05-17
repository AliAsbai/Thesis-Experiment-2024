#! /usr/bin/python3

def reverse_binary(n):
  """Reverses the binary representation of an integer.

  Args:
      n: The integer to be reversed.

  Returns:
      The integer representation of the reversed binary.
  """
  reversed_num = 0
  while n > 0:
    # Extract the least significant bit (LSB)
    last_bit = n & 1
    # Shift the reversed number left by 1 bit
    reversed_num = reversed_num << 1
    # Add the LSB to the reversed number
    reversed_num = reversed_num | last_bit
    # Remove the LSB from the original number
    n = n >> 1
  return reversed_num

# Read the input integer
n = int(input())

# Reverse the binary representation
reversed_n = reverse_binary(n)

# Print the result
print(reversed_n)
