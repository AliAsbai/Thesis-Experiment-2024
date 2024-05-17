#! /usr/bin/python3

import math

def minimum_days(n):
  """
  Calculates the minimum number of days needed to print n statues.

  Args:
      n: The number of statues to print (1 <= n <= 10000).

  Returns:
      The minimum number of days needed.
  """
  return math.ceil(math.log2(n)) + 1

# Read input
n = int(input())

# Print output
print(minimum_days(n))
