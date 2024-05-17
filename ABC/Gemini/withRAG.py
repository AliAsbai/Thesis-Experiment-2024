#! /usr/bin/python3

# Dictionary to map desired order letters to their position (A=0, B=1, C=2)
order_map = {"A": 0, "B": 1, "C": 2}

# Read the first line with the three numbers
numbers = [int(x) for x in input().split()]

# Read the second line with the desired order
desired_order = input()

# Create the output list to store results
output = [None] * 3

# Loop through desired order characters
for i in range(3):
  # Get the desired position for the current character
  desired_position = order_map[desired_order[i]]
  # Find the corresponding number based on position in sorted list
  for num in numbers:
    if sorted(numbers)[desired_position] == num:
      # Place the number in the output list based on desired order
      output[desired_position] = num
      break

# Print the output in one line with spaces
print(*output)
