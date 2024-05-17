def add_integers(a, b):
  """
  This function adds two integers a and b.

  Args:
      a: The first integer.
      b: The second integer.

  Returns:
      The sum of a and b.
  """

  return a + b

# Example usage:
# Get the two numbers from the user
first_number = int(input("Enter the first number (between 0 and 1000): "))
second_number = int(input("Enter the second number (between 0 and 1000): "))

# Call the function to add the numbers
sum = add_integers(first_number, second_number)

# Print the sum
print("The sum of", first_number, "and", second_number, "is", sum)
