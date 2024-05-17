#! /usr/bin/python3

def main():
  # Read input
  n, c = map(int, input().split())
  measurements = list(map(int, input().split()))

  # Initialize results with zeros
  results = [0] * n

  # First pass: find minimum value seen so far
  min_val = float('inf')
  for i in range(n):
    # Calculate difference adjusted for expected variation
    diff = measurements[i] - c * i

    # Update minimum and result
    min_val = min(min_val, diff)
    results[i] = max(results[i], diff - min_val)

  # Second pass: find maximum difference from negative side
  min_val = float('inf')
  for i in range(n - 1, -1, -1):
    # Calculate absolute difference adjusted for expected variation
    diff = abs(measurements[i]) + c * (i + 1)

    # Update minimum and result (similar to first pass)
    min_val = min(min_val, diff)
    results[i] = max(results[i], diff - min_val)

  # Print results
  print(*results)

if __name__ == "__main__":
  main()
