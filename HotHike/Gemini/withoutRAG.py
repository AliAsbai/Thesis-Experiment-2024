def find_best_hike_days(temperatures):
  """
  This function finds the best days to start a hike by minimizing the maximum
  temperature during the two hiking days.

  Args:
      temperatures: A list of integers representing daily maximum temperatures.

  Returns:
      A tuple containing two integers: the best day to start (inclusive) and the
      resulting maximum temperature for the two hiking days.
  """
  n = len(temperatures)
  best_day = 0
  min_max_temp = float('inf')  # Initialize with positive infinity

  for i in range(n - 2):
    # Calculate the maximum temperature for the two hiking days starting at i
    max_temp = max(temperatures[i], temperatures[i + 1])

    # Check if this starting day minimizes the maximum temperature
    if max_temp < min_max_temp:
      min_max_temp = max_temp
      best_day = i

  # Handle cases where all days have the same temperature
  if min_max_temp == temperatures[0]:
    return 1, min_max_temp  # Start on the first day in this case

  return best_day + 1, min_max_temp  # Return day (1-based) and max temperature

# Get input
n = int(input())
temperatures = [int(x) for x in input().split()]

# Find best days and print output
best_day, max_temp = find_best_hike_days(temperatures)
print(best_day, max_temp)
