#! /usr/bin/python3

# Read the number of meat types
n = int(input())

# Initialize a variable to track meat types
meat_types = set()

# Read each meat type and add it to the set
for _ in range(n):
  meat_type = input().strip()
  meat_types.add(meat_type)

# Determine Níels' order based on meat types
if len(meat_types) == 2:
  print("blandad best")  # Both types, "mixed best"
else:
  print(meat_types.pop())  # Print the only type or the first if multiple

