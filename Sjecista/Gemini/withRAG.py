#! /usr/bin/python3

def main():
  """
  Reads input from STDIN, calculates intersections, and prints the result.
  """
  n = int(input())
  intersections = 0
  for i in range(1, n - 3):
    for j in range(n - 2 - i, 0, -1):
      intersections += i * j
  print(intersections)

if __name__ == "__main__":
  main()
