def min_arrows(heights):
  """
  This function calculates the minimum number of arrows needed to pop all balloons.

  Args:
      heights: A list of integers representing the height of each balloon.

  Returns:
      An integer representing the minimum number of arrows needed.
  """
  if not heights:
    return 0

  # Find the maximum height among all balloons
  max_height = max(heights)

  # If all balloons have the same (maximum) height, we need one arrow per balloon
  if all(x == max_height for x in heights):
    return len(heights)

  stack = []
  arrows = 0

  for height in heights:
    # If the stack is empty or the current balloon is higher than the one on top
    # we need a new arrow to pop it.
    if not stack or height > stack[-1]:
      stack.append(height)
      arrows += 1
    # If the current balloon is lower than the one on top, it will be popped by
    # the existing arrow at the current height. We keep popping lower balloons
    # from the stack until we find a higher one.
    else:
      while stack and height < stack[-1]:
        stack.pop()
  
  return arrows

# Read the number of balloons
n = int(input())

# Read the balloon heights
heights = [int(x) for x in input().split()]

# Calculate the minimum number of arrows
min_arrows_needed = min_arrows(heights)

# Print the result
print(min_arrows_needed)
