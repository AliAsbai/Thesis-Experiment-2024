def closest_sum(numbers, target):
  """
  Finds the closest sum of two distinct numbers in the list to the target.

  Args:
      numbers: A list of distinct integers.
      target: The target number.

  Returns:
      The closest sum of two distinct numbers in the list to the target.
  """
  n = len(numbers)
  left, right = 0, n - 1
  closest_diff = float('inf')  # Initialize with positive infinity
  closest_sum = None

  # Check if target is smaller than the smallest element
  if target < numbers[left]:
    return target

  while left <= right:  # Handle case where left == right
    current_sum = numbers[left] + numbers[right]
    current_diff = abs(current_sum - target)

    if current_diff < closest_diff:
      closest_diff = current_diff
      closest_sum = current_sum

    if current_sum < target:
      left += 1
    elif current_sum > target:
      right -= 1
    else:  # Handle case where current_sum == target (both pointers on the same element)
      return target

  return closest_sum
