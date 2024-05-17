#! /usr/bin/python3

import math

def main():
  # Read smallest paper size and number of sheets for each size
  smallest_size = int(input())
  sheets = [int(x) for x in input().split()]

  # Calculate area needed for A1 paper
  a1_area = 2 ** (-7/4)

  # Initialize total area and tape length
  total_area = 0
  tape_length = 0

  # Iterate through paper sizes (largest to smallest)
  for size in range(smallest_size, 1, -1):
    area = 2 ** (- (7 - 2 * (size - 1)) / 4)
    sheet_area = sheets[size - 2] * area

    # Check if enough paper for A1
    if total_area + sheet_area >= a1_area:
      # Calculate tape length needed for current size
      tape_length += sheets[size - 2] * 2**(-(size - 2) / 4)
      break
    else:
      # Not enough paper, update total area
      total_area += sheet_area

  # Check if enough paper for A1
  if total_area >= a1_area:
    print(f"{tape_length:.10f}")
  else:
    print("impossible")

if __name__ == "__main__":
  main()
