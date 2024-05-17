from decimal import Decimal

def max_blue_lemonade(trades):
  """
  This function calculates the maximum amount of blue lemonade obtainable,
  considering exchange rates and capping the result at 10 liters with
  guaranteed precision.

  Args:
      trades: A list of tuples representing trades. Each tuple contains
              (offered_lemonade, desired_lemonade, exchange_rate).

  Returns:
      The maximum amount of blue lemonade obtainable (capped at 10 liters)
      as a string with a precision of 10^-6.
  """

  # Initialize current lemonade with high precision using Decimal
  current_lemonade = Decimal('1.0')

  # Loop through each trade
  for offered, desired, rate in trades:
    # Check if trade leads to blue lemonade
    if desired == "blue":
      # Calculate potential new amount using Decimal multiplication
      potential_amount = current_lemonade * Decimal(str(rate))

      # Update current lemonade if new amount is less than or equal to 10
      if potential_amount <= Decimal('10.0'):
        current_lemonade = potential_amount
      # Early return if new amount exceeds 10 (capped at 10 liters)
      else:
        return format(Decimal('10.0'), ".7f")  # Maximum amount reached

  # If no trade leads to blue lemonade, return 0 with high precision
  return format(Decimal('0.0'), ".7f")

# Read input data
num_children = int(input())
trades = []
for _ in range(num_children):
  offered, desired, rate = input().split()
  trades.append((offered, desired, float(rate)))

# Calculate and print the maximum blue lemonade
max_amount = max_blue_lemonade(trades)
print(max_amount)
