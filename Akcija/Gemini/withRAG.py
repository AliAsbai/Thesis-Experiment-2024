#! /usr/bin/python3

def calculate_min_price(prices):
  """
  Calculates the minimum price considering the promotional offer.

  Args:
      prices: A list of integers representing book prices.

  Returns:
      The minimum price the customer needs to pay.
  """
  prices.sort(reverse=True)  # Sort prices in descending order
  total_price = 0
  for i, price in enumerate(prices):
    if i % 3 != 2:  # Add prices for books not discounted
      total_price += price
  return total_price

# Read input
num_books = int(input())
prices = []
for _ in range(num_books):
  prices.append(int(input()))

# Calculate and print minimum price
min_price = calculate_min_price(prices.copy())  # Avoid modifying original list
print(min_price)
