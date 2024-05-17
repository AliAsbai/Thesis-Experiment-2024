#! /usr/bin/python3

for line in sys.stdin:
  # Access the first character (bit) of the input string
  bit = line[0]

  # Print the bit without conversion (already a string)
  print(bit)
