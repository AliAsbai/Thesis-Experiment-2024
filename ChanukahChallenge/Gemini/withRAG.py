#! /usr/bin/python3

def calculate_candles(days):
  """
  Calculates the number of candles needed for a Chanukah holiday lasting 'days'

  Args:
      days: The number of days for the Chanukah holiday

  Returns:
      The number of candles needed
  """
  # Formula for calculating total candles: (days * (days + 1)) / 2 + days (regular candles + shammas)
  return int((days * (days + 1)) / 2 + days)

# Read the number of data sets
num_datasets = int(input())

# Loop through each data set
for i in range(1, num_datasets + 1):
  # Read the number of days for this data set
  days = int(input())

  # Calculate and print the number of candles
  candles = calculate_candles(days)
  print(f"Case {i} - {candles}")
