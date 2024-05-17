#! /usr/bin/python3

import sys

# Read x and y coordinates
x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

# Determine the quadrant based on signs
if x > 0 and y > 0:
  quadrant = 1
elif x < 0 and y > 0:
  quadrant = 2
elif x < 0 and y < 0:
  quadrant = 3
else:
  quadrant = 4

# Print the quadrant number
print(quadrant)
