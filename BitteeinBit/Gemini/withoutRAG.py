def get_a_bit(bits):
  """
  This function takes a string of bits and returns any single bit from it.

  Args:
      bits: A string containing 0s and 1s representing bits.

  Returns:
      A single character '0' or '1' representing a bit from the input string.
  """

  # Select any character from the string
  return bits[0]

# Sample input strings
bits1 = "1"
bits2 = "00000"
bits3 = "101"

# Print the output for each sample input
print(get_a_bit(bits1))
print(get_a_bit(bits2))
print(get_a_bit(bits3))