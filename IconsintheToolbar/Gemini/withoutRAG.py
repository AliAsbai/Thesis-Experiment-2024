def min_toolbar_area(sizes):
  """
  Calculates the smallest possible area of a toolbar with 2 rows and N columns.

  Args:
      sizes: A sorted integer sequence (s1, ..., s2N) where si denotes the size of the i-th icon.

  Returns:
      The smallest possible area of the toolbar.
  """
  n = len(sizes) // 2  # Number of columns (half of the total icons)
  first_row = sizes[:n]  # Icons for the first row (largest N elements)
  second_row = sizes[n:]  # Icons for the second row (smallest N elements)

  # Width of the toolbar is the size of the biggest icon in the first row
  width = first_row[0]

  # Initialize heights with the largest elements in each row
  first_row_height = first_row[0]
  second_row_height = second_row[0]

  # Iterate through the icons in the first row, considering all elements
  for i in range(n):
    # Update the height of the first row based on current icon size
    first_row_height = max(first_row_height, first_row[i])

  # Iterate through the icons in the second row, considering all elements
  for i in range(n):
    # Update the height of the second row based on current icon size
    second_row_height = max(second_row_height, second_row[i])

  # Total area of the toolbar
  return width * (first_row_height + second_row_height)

# Read input
n = int(input())
sizes = []
for _ in range(2 * n):
  sizes.append(int(input()))

# Sort the sizes in descending order
sizes.sort(reverse=True)

# Calculate the minimum area
min_area = min_toolbar_area(sizes)

# Print the output
print(min_area)
