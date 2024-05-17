#! /usr/bin/python3

# Read input data
m, a, b, c = map(int, input().split())

# Check if it's possible to choose items without duplicates
if a + b + c <= 2 * m:
  print("possible")
else:
  print("impossible")
