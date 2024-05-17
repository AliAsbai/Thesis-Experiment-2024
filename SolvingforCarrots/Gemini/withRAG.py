#! /usr/bin/python3

# Read the first line containing contestants and total hufflepuff problems
contestants, total_problems = map(int, input().split())

# Total carrots awarded is the same as total problems solved
total_carrots = total_problems

# Skip reading contestant descriptions (not needed for this problem)
for _ in range(contestants):
  input()

# Print the total number of carrots
print(total_carrots)
