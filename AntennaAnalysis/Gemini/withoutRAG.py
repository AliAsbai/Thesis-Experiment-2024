def find_max_difference(data, c):
  """
  This function finds the most significant difference between the measurement on day i
  and any earlier day, after expected variations are taken into account.

  Args:
      data: A list of integers representing the 5G measurements for n days.
      c: An integer representing the expected day-to-day variation.

  Returns:
      A list of integers where yi represents the most significant difference on day i.
  """
  n = len(data)
  # Initialize result list with 0s for all days
  result = [0] * n

  # Track the minimum value seen so far (excluding expected difference)
  min_val = float('inf')

  for i in range(n):
    # Calculate the expected difference for day i
    expected_diff = c * i

    # Update result for current day (consider both positive and negative differences)
    result[i] = max(result[i], data[i] - min_val - expected_diff, min_val - data[i] + expected_diff)

    # Update minimum value if necessary (consider both positive and negative differences)
    min_val = min(min_val, data[i] + expected_diff, data[i] - expected_diff)

  return result

# Example usage
data = [2, 7, 1, 5, 4]
c = 1

max_differences = find_max_difference(data, c)

# Print the results
for i, diff in enumerate(max_differences):
  print(f"Day {i+1}: {diff}")
