#! /usr/bin/python3

# Read input as integers
a, b, c, n = map(int, input().split())

# Check if it's possible to create a problemset
if (a == 0 or b == 0 or c == 0 or  # At least one of each difficulty
    a + b + c < n or  # Total problems less than required
    n < 3):  # Needs at least 3 problems
  print("NO")
else:
  print("YES")
