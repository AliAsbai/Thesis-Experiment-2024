def find_cooking_time(entry_times, exit_times):
  """
  This function finds the secret cooking time that maximizes the number of 
  consistent time differences between entry and exit timestamps, considering faulty detectors.

  Args:
      entry_times: A list of integers representing entry timestamps (ms).
      exit_times: A list of integers representing exit timestamps (ms).

  Returns:
      The best guess of the secret cooking time (ms) with the most consistent time differences.
  """
  
  # Initialize variables
  time_differences = []
  best_time = None
  best_consistency = 0

  # Calculate all possible time differences between entry and exit timestamps
  for i in range(len(entry_times)):
    for j in range(len(exit_times)):
      time_difference = exit_times[j] - entry_times[i]
      time_differences.append(time_difference)

  # Count occurrences of each time difference
  time_diff_counts = {}
  for diff in time_differences:
    time_diff_counts[diff] = time_diff_counts.get(diff, 0) + 1

  # Find the time difference with the most occurrences (potentially multiple)
  max_count = max(time_diff_counts.values(), default=0)
  for diff, count in time_diff_counts.items():
    if count == max_count:
      # If multiple time differences have the same max count, choose the smallest
      if best_time is None or diff < best_time:
        best_time = diff
        best_consistency = count

  return best_time

# Read input
n = int(input())
m = int(input())
entry_times = [int(x) for x in input().split()]
exit_times = [int(x) for x in input().split()]

# Find and print the secret cooking time
secret_time = find_cooking_time(entry_times, exit_times)
print(secret_time)
