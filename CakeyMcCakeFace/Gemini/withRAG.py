#! /usr/bin/python3
import sys

def main():
  # Read input
  n = int(sys.stdin.readline())
  m = int(sys.stdin.readline())
  entry_times = [int(x) for x in sys.stdin.readline().strip().split()]
  exit_times = [int(x) for x in sys.stdin.readline().strip().split()]

  # Calculate all possible time differences
  diffs = {}
  for entry_time in entry_times:
    for exit_time in exit_times:
      diff = exit_time - entry_time
      if diff >= 0:  # Only consider positive or zero differences
        diffs[diff] = diffs.get(diff, 0) + 1

  # Find the most frequent positive difference (smallest if multiple)
  max_count, best_diff = 0, None
  for diff, count in diffs.items():
    if count > max_count:
      max_count = count
      best_diff = diff
    elif count == max_count and diff < best_diff:
      best_diff = diff

  # Print output
  print(best_diff or 0)  # Print 0 if no positive difference found

if __name__ == "__main__":
  main()
