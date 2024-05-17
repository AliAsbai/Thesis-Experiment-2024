def min_price(prices):
  """
  Calculates the minimum price for a customer buying books with a "Take 3, pay for 2" offer.

  Args:
      prices: A list of integers representing the prices of the books.

  Returns:
      The minimum price the customer needs to pay.
  """
  # Sort the prices in ascending order.
  prices.sort()

  total_price = 0
  # Group counter keeps track of the number of books in the current group.
  group_counter = 0

  for price in prices:
    # Add the price to the total if it's not the cheapest book in a group of 1 or 2.
    if group_counter < 2 or price != prices[0]:
      total_price += price
      group_counter += 1
    # Reset the counter for the next group.
    if group_counter == 3:
      group_counter = 0

  return total_price

# Read the number of books.
num_books = int(input())

# Read the book prices.
prices = []
for _ in range(num_books):
  prices.append(int(input()))

# Calculate and print the minimum price.
min_price_value = min_price(prices)
print(min_price_value)
