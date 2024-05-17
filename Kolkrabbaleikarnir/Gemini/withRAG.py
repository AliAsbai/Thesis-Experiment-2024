#! /usr/bin/python3
import sys
from math import log2

def solve(n, m):
  c = [0.5]  # Initial probability for Hlini crossing the first tile
  for i in range(1, min(n, m)):  # Loop iterates up to m-1 (excluding last step)
    val = log2(n - i) - log2(i + 1)
    if val < -1e-7:
      break
    c.append(c[-1] + val)
  ans = 0
  for k in range(m - len(c) + 1, m + 1):
    ans += k * c[m - k] * (1 / n) ** n
  return ans

def main():
  line = sys.stdin.readline().strip().split()
  n, m = int(line[0]), int(line[1])
  print(solve(n, m))

if __name__ == "__main__":
  main()
