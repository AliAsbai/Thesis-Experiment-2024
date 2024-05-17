# Read input from the user
input_str = input("Enter two integers separated by space: ")

# Split the input string into two integers
a, b = map(int, input_str.split())

# Add the two integers
sum_result = a + b

# Print the sum
print(sum_result)
