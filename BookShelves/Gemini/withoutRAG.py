def min_shelves(small_books, medium_books, big_books, shelf_width):
  """
  Calculates the minimum number of shelves needed to store all books.

  Args:
      small_books: Number of small books (width 1).
      medium_books: Number of medium books (width 2).
      big_books: Number of big books (width 3).
      shelf_width: Width of a single shelf (must be positive).

  Returns:
      The minimum number of shelves required.

  Raises:
      ValueError: If the shelf_width is not positive.
  """

  # Calculate total space needed for each book size
  small_space = small_books * 1
  medium_space = medium_books * 2
  big_space = big_books * 3

  # Calculate total space needed for all books
  total_space = small_space + medium_space + big_space

  # Validate shelf width (must be positive)
  if shelf_width <= 0:
    raise ValueError("Shelf width must be a positive integer.")

  # Handle empty bookshelf scenario (no books)
  if total_space == 0:
    return 2  # Minimum of 2 shelves even for no books

  # Divide total space by shelf width, rounding up for any remaining space
  min_shelves = int((total_space + shelf_width - 1) / shelf_width)

  return min_shelves

# Read input data
small_books, medium_books, big_books = map(int, input().split())
shelf_width = int(input())

try:
  # Calculate and ensure at least 2 shelves
  min_shelves = max(2, min_shelves(small_books, medium_books, big_books, shelf_width))

  # Print the minimum number of shelves
  print(min_shelves)
except ValueError as e:
  print("Error:", e)
