#! /usr/bin/python3

def find_best_hike_days(temperatures):
  """Finds the best days to start a hike to minimize maximum temperature.

  Args:
      temperatures: A list of integers representing daily maximum temperatures.

  Returns:
      A tuple containing the starting day (index) and the maximum temperature
      during the two hiking days.
  """

  n = len(temperatures)
  min_max_temp = float('inf')  # Initialize with positive infinity
  best_start_day = None

  for start_day in range(2, n):
    # Get the maximum temperature during the two hiking days (current and two days prior)
    max_temp = max(temperatures[start_day], temperatures[start_day - 2])
    if max_temp < min_max_temp:
      min_max_temp = max_temp
      best_start_day = start_day - 1  # Day before the current hiking day

  return best_start_day, min_max_temp

# Read input
n = int(input())
temperatures = [int(x) for x in input().split()]

# Find best days for hike
best_day, max_temp = find_best_hike_days(temperatures)

# Print output
print(best_day, max_temp)

if __name__ == "__main__":
  find_best_hike_days(temperatures)
